#! /usr/bin/env python3 

class DayOfTheWeek:
    """The days of the week."""
    
    def __init__(self, day: str) -> None:
        self.day = day
        
    def name(self) -> str:
        """Return name of day."""
        dict_days = {'Mon': 'Monday', 
                     'Thu': 'Thursday', 
                     'Wed': 'Wedneday', 
                     'Thr': 'Thursday', 
                     'Fri': 'Friday', 
                     'Sat': 'Saturday', 
                     'Sun': 'Sunday',}
        if self.day in dict_days:
            return dict_days[self.day]
        else: 
            return f'No days {self.day}'
        
    def __str__(self) -> str:
        return str(self.name)

my_day = DayOfTheWeek('Sun')
print(my_day.name())

    
    