#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GREP WITH THREADING-->"""

import optparse
import os 
import queue
import threading


#maximum length word
BLOCK_SIZE = 8000

class Worker(threading.Thread):
    """Working with threading"""
    
    def __init__(self, work_queue, word: str, number: int) -> None:
        super().__init__()
        self.work_queue = work_queue
        self.word = word 
        self.number = number
        
    def run(self) -> None:
        """Run task"""
        
        while True:
            try:
                filename = self.work_queue.get()
                self.process(filename)
            finally:
                self.work_queue.task_done()
                
    def process(self, filename: str) -> None:
        """Start process reading files"""
        
        #start
        previous = ''
        try:
            with open(filename, 'rb') as fh:
                while True:
                    current = fh.read(BLOCK_SIZE)
                    if not current:
                        break
                    current = current.decode('utf8', 'ignore')
                    if (self.word in current or self.word in previous[-len(self.word):] + current[:len(self.word)]):
                        print(f'{self.number}{filename}')
                        break
                    
                    if len(current) != BLOCK_SIZE:
                        break
                    previous = current
        except EnvironmentError as err:
            print(f'{self.number}{err}')
            
def parse_options() -> list:
    """Command line parsing"""
    
    parser = optparse.OptionParser(
            usage=("usage: %prog [options] word name1 "
                   "[name2 [... nameN]]\n\n"
                   "names are filenames or paths; paths only "
                   "make sense with the -r option set"))
    parser.add_option("-t", "--threads", dest="count", default=7,
            type="int",
            help=("the number of threads to use (1..20) "
                  "[default %default]"))
    parser.add_option("-r", "--recurse", dest="recurse",
            default=False, action="store_true",
            help="recurse into subdirectories")
    parser.add_option("-d", "--debug", dest="debug", default=False,
                      action="store_true")
    opts, args = parser.parse_args()
    if len(args) == 0:
        parser.error("a word and at least one path must be specified")
    elif len(args) == 1:
        parser.error("at least one path must be specified")
    if (not opts.recurse and
        not any([os.path.isfile(arg) for arg in args])):
        parser.error("at least one file must be specified; or use -r")
    if not (1 <= opts.count <= 20):
        parser.error("thread count must be 1..20")
    return opts, args[0], args[1:]


def get_files(args: list, recurse: str) -> list:
    """parsing files and formation filelist"""
    
    filelist = []
    for path in args:
        if os.path.isfile(path):
            filelist.append(path)
        elif recurse:
            for root, dirs, files in os.walk(path):#TODO !not used ->dirs<-
                for filename in files:
                    filelist.append(os.path.join(root, filename))
    return filelist


def main() -> None:
    """Main function"""
    
    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    work_queue = queue.Queue()
    for i in range(opts.count):
        number = f'{i + 1}: ' if opts.debug else ''
        worker = Worker(work_queue, word, number)
        worker.daemon = True
        worker.start()
    for filename in filelist:
        work_queue.put(filename)
    work_queue.join()
    
if __name__ == '__main__':
    main()