#! /usr/bin/env python3 

from flask import Flask
from flask import render_template
from pathlib import Path

app = Flask(__name__)

class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

# skipe
def is_not_hidden(path):
    return not path.name.startswith(".")

dirs = ['a_bite_of_everything', 
        'algo',
        'astronomy_and_phisics',
        'asyncio',
        'browser',
        'cases',
        'ci_cd',
        'cs',
        'dash',
        'django_and_drf',
        'docker',
        'dragon_area',
        'fastapi',
        'flask',
        'futures',
        'leetcode',
        'microservices',
        'ml_dl_ai',
        'mongodb',
        'my_env',
        'my_lang',
        'OOP_ADVANCED',
        'opencv',
        'patterns',
        'python10',
        'recipes',
        'recursi',
        'repeat',
        'std_lib',
        'styles',
        'tasks',
        'tests',
        ]

for directory in dirs:
    paths = DisplayablePath.make_tree(Path(directory), criteria=is_not_hidden)
    """for path in paths:
        print(path.displayable())"""

@app.route('/')
def index(dirs=dirs):
    for directory in dirs:
        paths = DisplayablePath.make_tree(Path(directory), criteria=is_not_hidden)
    return render_template('main.html', paths=paths)



if __name__ == '__main__':
    app.run(port=5555, debug=True)