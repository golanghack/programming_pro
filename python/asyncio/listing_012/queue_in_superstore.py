#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue
from random import randrange
from typing import List 

class Product:
    
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time
        
class Customer:
    
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products
        
async def checkout_customer(queue: Queue, cashier_number: int):
    # as long as there is someone in the queue
    # choose a buyer
    while not queue.empty():
        customer: Customer = queue.get_nowait()
        print(f'Cashier {cashier_number} service {customer.customer_id}')
    
        for product in customer.products:
            # working every products 
            print(f'Cashier {cashier_number} service {customer.customer_id} -> {product.name}')
            await asyncio.sleep(product.checkout_time)
    
        print(f'cashier {cashier_number} service ended for customer {customer.customer_id}')
        queue.task_done()
    
async def main():
    customer_queue = Queue()
    all_products = [Product('beer', 2), 
                    Product('banana', .5), 
                    Product('becon', .2), 
                    Product('pampers', .2),]
    
    # create 10 sporadic customers with sporadic products
    for i in range(10):
        products = [all_products[randrange(len(all_products))]
                    for _ in range(randrange(10))]
        customer_queue.put_nowait(Customer(i, products))
    # create 3 cashiers
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i))
                    for i in range(3)]
        
    await asyncio.gather(customer_queue.join(), *cashiers)
        
asyncio.run(main())
        
