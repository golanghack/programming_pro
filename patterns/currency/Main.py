#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SINGLETON-->"""


import os 
import sys 
import urllib
import tkinter as tk 
import tkinter.ttk as ttk 
import tkinter.messagebox as messagebox 
Spinbox = ttk.Spinbox if hasattr(ttk, 'Spinbox') else tk.Spinbox 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Rates 
import TKUtul


class Window(ttk.Frame):
    
    
    def __init__(self, master=None) -> None:
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.create_bindings()
        self.currencyFromCombobox.focus()
        self.after(10, self.get_rates)
        
    
    def create_variables(self) -> None:
        """Creating custom variable"""
        
        self.currency_from = tk.StringVar()
        self.currency_to = tk.StringVar()
        self.amount = tk.StringVar()
        self.rates = {}
        
    def get_rates(self) -> None:
        """Get rates functions"""
        
        try:
            self.rates = Rates.get()
            self.populate_comboboxes()
        except urllib.error.URLError as err:
            messagebox.showerror('Curent \u2014 Error', str(err), parent=self)
            self.quit()
            
            
    def populate_comboboxes(self) -> None:
        """creating calculations"""
        
        currencies = sorted(self.rates.keys())
        for combobox in (self.currency_from_combobox, self.currency_to_combobox):
            combobox.state(('readonly',))
            combobox.config(values=currencies)
        TKUtul.set_combobox_item(self.currency_from_combobox, 'USD', True)
        TKUtul.set_combobox_item(self.currency_to_combobox, 'GBP', True)
        self.calculate()
        
    
    def create_widgets(self) -> None:
        """WIDGETS TTK"""
        
        self.currency_from_combobox = ttk.Combobox(self, textvariable=self.currency_from)
        self.currency_to_combobox = ttk.Combobox(self, textvariable=self.currency_to)
        self.amount_spinbox = Spinbox(self, textvariable=self.amount, from_=1.0, to=10e6, validate='all', format='%0.2f', width=8)
        self.amount_spinbox.config(validatecommand=(self.amount_spinbox.register(self.validate), '%P'))
        self.result_label = ttk.Label(self)
        
        
    def validate(self, number: float) -> bool:
        return TKUtul.validate_spinbox_float(self.amount_spinbox, number)
    
    def create_layout(self) -> None:
        padWE = dict(sticky=(tk.W, tk.E), padx='0.5m', pady='0.5m')
        self.currency_from_combobox.grrid(row=0, column=0, **padWE)
        self.amount_spinbox.grid(row=0, column=1, **padWE)
        self.currency_to_combobox.grid(row=1, column=0, **padWE)
        self.result_label.grid(row=1, column=1, **padWE)
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(150, 40)
        
        
    def create_bindings(self):
        self.currency_from_combobox.bind('<<ComboboxSelected>>', self.calculate)
        self.currency_to_combobox.bind('<<ComboboxSelected>>', self.calculate)
        self.amount_spinbox.bind('<Return>', self.calculate)
        self.master.bind('<Escape>', lambda event: self.quit())
        
        
    def calculate(self, event=None):
        from_currency = self.currency_from.get()
        to_currency = self.currency_to.get()
        amount = self.amount.get()
        if from_currency and to_currency and amount:
            amount = ((self.rates[from_currency] / self.rates[to_currency]) * float(amount))
            self.result_label.config(text=f'{amount:,.2f}')
            
if __name__ == '__main__':
    if sys.stdout.isatty():
        app = tk.Tk()
        app.title('Window')
        Window(app)
        app.mainloop()
    else:
        print('Loaded OK')
        
        
        