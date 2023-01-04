#! /usr/bin/env python3 

"""<--DECORATOR-->"""


import collections


def main():
    form = Form()
    test_user_interaction_with(form)
    
class Form:
    """Base form class"""
    
    def __init__(self):
        self.create_widgets()
        self.create_mediator()
        
    
    def create_widgets(self):
        self.name_text = Text()
        self.email_text = Text()
        self.ok_button = Button('OK')
        self.cansel_button = Button('Cancel')
        
    def create_mediator(self):
        self.mediator = Mediator(((self.name_text, self.update_ui), 
                                  (self.email_text, self.update_ui),
                                  (self.ok_button, self.clicked),
                                  (self.cansel_button, self.clicked)))
        self.update_ui
        
    def update_ui(self, widget=None):
        self.ok_button.enabled = (bool(self.name_text.text) and bool(self.email_text.text))
        
    def clicked(self, widget):
        if widget == self.ok_button:
            print('OK')
        if widget == self.cansel_button:
            print('Cancel')
            
class Mediator:
    
    
    def __init__(self, widget_callable_pairs):
        self.callables_for_widget = collections.defaultdict(list)
        for widget, caller in widget_callable_pairs:
            self.callables_for_widget[widget].append(caller)
            widget.mediator = self
            
    def on_changed(self, widget):
        callables = self.callables_for_widget.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError(f'No on_change() method registered for {widget}')
        
        
class Mediated:
    
    def __init__(self):
        self.mediator = None
        
    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)
            
            
class Button(Mediated):
    
    def __init__(self, text=''):
        super().__init__()
        self.enabled = True
        self.text = text 
        
    
    def click(self):
        if self.enabled:
            self.on_change()
            
    def __str__(self):
        return f'Button ({self.text!r} {"enabled" if self.enabled else "disabled"}'
    
    
class Text(Mediated):
    
    def __init__(self, text=''):
        super().__init__()
        self.__text = text  
        
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        if self.text != text:
            self.__text = text
            self.on_change()
            
    def __str__(self):
        return f'Text ({self.text!r}'
    
def test_user_interaction_with(form):
    form.ok_button.click()
    print(form.ok_button.enabled)
    
    form.name_text.text = 'Fred'
    print(form.ok_button.enabled)
    
    form.email_text.text = 'fred@bloggers.com'
    print(form.ok_button.enabed)
    
    form.ok_button.click()
    form.email_text.text = ''
    print(form.ok_button.enabled)
    
    form.cancel_button.click()
    
    
if __name__ == '__main__':
    main()