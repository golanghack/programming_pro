#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--BUILDER PATTERN-->"""

import abc 
import os 
import re 
import sys 
import tempfile
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape
    
def main():
    #regress tests
    if len(sys.argv) > 1 and sys.argv[1] == '-P':
        print(create_login_form(HtmlFormBuilder()))
        print(create_login_form(TkFormBuilder()))
        return
    html_filename: str = os.path.join(tempfile.gettempdir(), 'login.html')
    html_form: str = create_login_form(HtmlFormBuilder())
    with open(html_filename, 'w', encoding='utf-8') as file:
        file.write(html_form)
    print('wrote', html_filename)
    
    tk_filename = os.path.join(tempfile.gettempdir(), 'login.py')
    tk_form = create_login_form(TkFormBuilder())
    with open(tk_filename, 'w', encoding='utf-8') as file:
        file.write(tk_form)
    print('wrote', tk_filename)
    
    
def create_login_form(builder):
    builder.add_title('Login')
    builder.add_label('Username', 0, 0, target='username')
    builder.add_entry('username', 0, 1)
    builder.add_label('Password', 1, 0, target='password')
    builder.add_entry('Password', 1, 1, kind='password')
    builder.add_button('Login', 2, 0)
    builder.add_button('Cancel', 2, 1)
    return builder.form()


class AbstractFormBuilder(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def add_title(self, title: str) -> None:
        self.title = title
        
    @abc.abstractmethod
    def form(self) -> None:
        pass
    
    @abc.abstractmethod
    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        pass
    
    @abc.abstractmethod
    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        pass
    
    @abc.abstractmethod
    def add_button(self, text: str, row: int, column: int, **kwargs) -> None:
        pass
    
class HtmlFormBuilder(AbstractFormBuilder):
    
    def __init__(self) -> None:
        self.title = 'HtmlFormBuilder'
        self.items = {}
        
    def add_title(self, title: str) -> None:
        super().add_title(escape(title))
        
    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        self.items[(row, column)] = ('<td><label for="{}">{}:</label></td>'
                                     .format(kwargs['target'], escape(text)))
        
    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        html = """<td><input name'{}' type='{}'/></td>""".format(variable, kwargs.get('kind', 'text'))
        self.items[(row, column)] = html 
        
    def add_button(self, text: str, row: int, column: int, **kwargs) -> None:
        html = """<td><input type='submit' value='{}'/></td>""".format(escape(text))
        self.items[(row, column)] = html
        
    
    def form(self) -> str:
        html = ["<!doctype html>\n<html><head><title>{}</title></head>"
                "<body>".format(self.title), '<form><lable border="0">']
        this_row = None
        for key, value in sorted(self.items.items()):
            row, column = key 
            if this_row is None:
                html.append(' <tr>')
            if this_row != row:
                html.append(' </tr>\n <tr>')
            this_row = row 
            html.append('    ' + value)
        html.append('  </tr>\n</table></form></body></html>')
        return '\n'.join(html)
    
class TkFormBuilder(AbstractFormBuilder):
    
    TEMPLATE = """#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class {name}Form(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.withdraw()     # hide until ready to show
        self.title("{title}")
        {statements}
        self.bind("<Escape>", lambda *args: self.destroy())
        self.deiconify()    # show when widgets are created and laid out
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

if __name__ == "__main__":
    application = tk.Tk()
    window = {name}Form(application)
    application.protocol("WM_DELETE_WINDOW", application.quit)
    application.mainloop()
"""

    def __init__(self) -> None:
        self.title = 'TkFormBuilder'
        self.statements = []
        
    def add_title(self, title: str) -> None:
        return super().add_title(title)

    
    def add_label(self, text: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(text)
        create = f"""self.{name}Label = ttk.Label(self, text='{text}:')"""
        layout = f"""self.{name}Label.grid(row={row}, column={column}, sticky=tk.W, padx='0.75m',
        pady='0.75')"""
        self.statements.extend((create, layout))
        
    def add_entry(self, variable: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(variable)
        extra = "" if kwargs.get('kind') != 'password' else ', show="*"'
        create = f'self.{name}Entry = ttk.Entry(self{extra})'
        layout = f"""self.{name}Entry.grid(row={row}, column={column}, sticky=(tk.W, tk.E), padx="0.75m", pady="0.75m")"""   
        self.statements.extend((create, layout))
        
    def add_button(self, text: str, row: int, column: int, **kwargs) -> None:
        name = self._canonicalize(text)
        create = f"""self.{name}Button = ttk.Button(self, text='{text}')"""
        layout = f"""self.{name}Button.grid(row={row}, column={column}, padx='0.75m',
pady='0.75m')"""
        self.statements.extend((create, layout))
        
    def form(self):
        return TkFormBuilder.TEMPLATE.format(title=self.title, 
                                             name=self._canonicalize(self.title, False), 
                                             statements='\n        '.join(self.statements))
        
    def _canonicalize(self, text: str, start_lower: bool=True) -> str:
        text = re.sub(r'\W+', '', text)
        if text[0].isdigit():
            return '_' + text
        return text if not start_lower else text[0].lower() + text[1:]
    
if __name__ == '__main__':
    main()
        
    
