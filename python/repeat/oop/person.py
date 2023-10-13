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
        
class Manager:
    def __init__(self, name: str, pay: float = 0) -> None:
        self.person = Person(name, 'mngr', pay)
        
    def give_raise(self, percent: float, bonus: float=0.10):
        self.person.give_raise(percent + bonus)
        
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return str(self.person)
    
class Department:
    
    def __init__(self, *args):
        self.members = list(args)
    
    def add_member(self, person):
        self.members.append(person)
    
    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)
    
    def show_all(self):
        for person in self.members:
            print(person)
            
            
    
if __name__ == '__main__':
    #testing
    tom = Manager('Tom', 5000.0)
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
    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raise(0.10)
    development.show_all()