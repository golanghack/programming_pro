#! /usr/bin/env python3 

class Person:
    """people"""
    
    def __init__(self, name: str, job: str=None, pay: float=0) -> None:
        """Constructor Person"""
        
        self.name = name
        self.job = job
        self.pay = pay 
        
    def last_name(self):
        """Return last name in list names with [-1] index logic"""
        
        return self.name.split()[-1]
    
    def give_raise(self, percent: float):
        """Return new pay with raise"""
        
        self.pay = int(self.pay * (1 + percent))
        
    def __repr__(self) -> str:
        return f'[Person -> {self.name}, Pay -> {self.pay}]'
        
class Manager(Person):
    def __init__(self, name: str, pay: float = 0) -> None:
        Person.__init__(self, name, 'mngr', pay)
        
    def give_raise(self, percent: float, bonus: float=0.10):
        Person.give_raise(self, percent + bonus)
    
if __name__ == '__main__':
    #testing
    tom = Manager('Tom', 'mngr', 5000.0)
    tom.give_raise(0.10)
    print(tom)
    print(tom.last_name)
    bob = Person('Bob')
    sue = Person('Sue', job='dev', pay=100000)
    print(bob.name, bob.job, bob.pay)
    print(sue.name, sue.job, sue.pay)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)
    
    print('<-----ALL----->')
    for obj in (bob, tom, sue):
        obj.give_raise(0.10)
        print(obj)