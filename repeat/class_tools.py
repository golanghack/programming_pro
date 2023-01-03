#! /usr/bin/env python3

class AttrDisplay:
    """ 
    Provides an inherited mapping overload method that exposes
    instances with their class names and name=value pairs for each attribute,
    stored in the instance itself (but not attributes inherited from its classes) .
    Can be connected to any class and will work on any instance.
    """
    
    def gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)
    
    def __repr__(self) -> str:
        return f'[{self.__class__.__name__} -> {self.gather_attrs()}]'
    
if __name__ == '__main__':
    class Test(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = Test.count
            self.attr2 = Test.count + 1
            Test.count += 2
            
    class SubTest(Test):
        pass
    
    x, y = Test(), SubTest()
    print(x)
    print(y)