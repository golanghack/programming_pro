#! /usr/bin/env python3 

class Person:
    """people"""
    
    def __init__(self, name: str, job: str=None, pay: float=0) -> None:
        """Constructor Person"""
        
        self.name = name
        self.job = job
        self.pay = pay 


if __name__ == '__main__':
    #testing
    bob = Person('Bob')
    sue = Person('Sue', job='dev', pay=100000)
    print(bob.name, bob.job, bob.pay)
    print(sue.name, sue.job, sue.pay)