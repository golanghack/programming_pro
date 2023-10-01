#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue
from random import randrange

class Product:
    
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time
        
class Customer:
    
    def __init__(self, custormer_id: int, products: Product):
        self.customer_id = custormer_id
        self.products = products
        
async def checkout_customer(queue: Queue, cashier_number: int):
    while True:
        customer: Customer = await queue.get()
        print(f'cashier {cashier_number} service customer {customer.customer_id}')
        
        for product in customer.products:
            print(f'cashier {cashier_number} service {customer.customer_id} -> {product.name}')
            await asyncio.sleep(product.checkout_time)
        
        print(f'cashier {cashier_number} ended service customer {customer.customer_id}')
        queue.task_done()
        
        
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beer', 2),
                    Product('banana', .5), 
                    Product('becon', .2),
                    Product('pampers', .2),]
    products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    return Customer(customer_id, products)


async def customer_generator(queue: Queue):
    customer_count = 0 
    
    while True:
        customers = [generate_customer(i) for i in range(customer_count, customer_count + randrange(5))]
        for customer in customers:
            print('Waiting possible customer to queue')
            await queue.put(customer)
            print('Customer into queue')
        customer_count = customer_count + len(customers)
        await asyncio.sleep(1)
        
async def main():
    customer_queue = Queue(5)
    customer_producer = asyncio.create_task(customer_generator(customer_queue))
    
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) 
                for i in range(3)]
    await asyncio.gather(customer_producer, *cashiers)
    
asyncio.run(main())