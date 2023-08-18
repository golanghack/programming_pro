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

import collections


def main():
    form = Form()
    test_user_interaction_with(form)


class Form:

    def __init__(self):
        self.create_widgets()
        self.create_mediator()


    def create_widgets(self):
        self.name_text = Text()
        self.email_text = Text()
        self.ok_button = Button("OK")
        self.cancel_button = Button("Cancel")


    def create_mediator(self):
        self.mediator = Mediator(((self.name_text, self.update_ui),
                (self.email_text, self.update_ui),
                (self.ok_button, self.clicked),
                (self.cancel_button, self.clicked)))
        self.update_ui()


    def update_ui(self, widget=None):
        self.ok_button.enabled = (bool(self.name_text.text) and
                                 bool(self.email_text.text))


    def clicked(self, widget):
        if widget == self.ok_button:
            print("OK")
        elif widget == self.cancel_button:
            print("Cancel")


class Mediator:

    def __init__(self, widgetCallablePairs):
        self.callablesForWidget = collections.defaultdict(list)
        for widget, caller in widgetCallablePairs:
            self.callablesForWidget[widget].append(caller)
            widget.mediator = self


    def on_change(self, widget):
        callables = self.callablesForWidget.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError(f'No on_change() method registered for {widget}')


def mediated(Class):
    setattr(Class, "mediator", None)
    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)
    setattr(Class, "on_change", on_change)
    return Class


@mediated
class Button:

    def __init__(self, text=""):
        super().__init__()
        self.enabled = True
        self.text = text
    

    def click(self):
        if self.enabled:
            self.on_change()


    def __str__(self):
        return f'Button({self.text!r}) {"enabled" if self.enabled else "disablerd"}'


@mediated
class Text:

    def __init__(self, text=""):
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
    form.ok_button.click()           
    print(form.ok_button.enabled)  
    form.name_text.text = "Fred"
    print(form.ok_button.enabled)   
    form.email_text.text = "fred@bloggers.com"
    print(form.ok_button.enabled)    
    form.ok_button.click()           
    form.email_text.text = ""
    print(form.ok_button.enabled)    
    form.cancel_button.click()       


if __name__ == "__main__":
    main()