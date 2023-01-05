#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--MEDIATOR-->"""

from Utils import corutine

def main():
    form = Form()
    test_user_interaction_with(form)
    
class Form:
    
    def __init__(self) -> None:
        self.create_widgets()
        self.create_mediator()
        
    def create_widgets(self):
        self.name_text = Text()
        self.email_text = Text()
        self.ok_button = Button('OK')
        self.cancel_button = Button('Cancel')
        
    def create_mediator(self):
        self.mediator = self._update_ui_mediator(self._clicked_mediator())
        for widget in (self.name_text, self.email_text, self.ok_button, self.cancel_button):
            widget.mediator = self.mediator
            
        self.mediator.send(None)
        
    @corutine
    def _update_ui_mediator(self, successor=None):
        while True:
            widget = (yield)
            self.ok_button.enabled = (bool(self.name_text.text) and bool(self.email_text.text))
            if successor is not None:
                successor.send(widget)
                
    @corutine
    def _clicked_mediator(self, successor=None):
        while True:
            widget = (yield)
            if widget == self.ok_button:
                print('OK')
            if widget == self.cancel_button:
                print('Cancel')
            if successor is not None:
                successor.send(widget)
                
                
class Mediated:
    
    def __init__(self):
        self.mediator = None
        
        
    def on_change(self):
        if self.mediator is not None:
            self.mediator.send(self)
            
    
class Button(Mediated):
    
    def __init__(self, text=''):
        super().__init__()
        self.enabled = True
        self.text = text 
        
    def click(self):
        if self.enabled:
            self.on_change()
            
    def __str__(self):
        return f'Button ({self.text!r}) {"enabled" if self.enabled else "disabled"}'
    
class Text(Mediated):
    
    def  __init__(self, text=''):
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
        return f'Text({self.text!r})'
    
def test_user_interaction_with(form):
    form.okButton.click()           
    print(form.okButton.enabled)    
    form.nameText.text = "Fred"
    print(form.okButton.enabled)    
    form.emailText.text = "fred@bloggers.com"
    print(form.okButton.enabled)    
    form.okButton.click()           
    form.emailText.text = ""
    print(form.okButton.enabled)    
    form.cancelButton.click()      