#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import math
import sys
import os
import itertools

def print_usage():
    
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision, syntax, StopIteration, \n")
    sys.stderr.write("\tkeyboard, GeneratorExit\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    f = 3
    assert f== 4
elif error_type == "io":
    f = open('myfile.txt')
elif error_type == "import":
    import Config as CF
elif error_type == "index":
    spam = ['cat', 'dog', 'mouse']
    print(spam[6])
elif error_type == "key":
    spam = {'cat': 'Kit', 'dog': 'Dawg'}
    print('The name of my pet giraffe is' + spam['zebra'])
elif error_type == "name":
    hoopla = 'Paul'
    print('My name is ' + hoopl)
elif error_type == "os":
   for i in range(10):
       print i, os.ttyname(i)
elif error_type == "type":
    x = '2' + 2
elif error_type == "value":
    x = int(input("Please enter a number: "))
elif error_type == "zerodivision":
    x = 1/0
elif error_type == "StopIteration":
    l = [0, 1, 2]
    i = iter(l)
    print i
    print i.next()
    print i.next()
    print i.next()
    print i.next()
elif error_type == "GeneratorExit":
    def my_generator():
        try:
            for i in range(5):
                print 'Yielding', i
                yield i
        except GeneratorExit:
             print 'Exiting Early'

    g = my_generator()
    print g.next()
    g.close()
elif error_type == "keyboard":
    try:
        print 'Press Retuen or Ctrl-C:',
        ignored = raw_input()
    except Exception, err:
        print 'Caught exception:', err
    except KeyboardInterrupt, err:
        print 'Caught KeyboardInterrupt'
    else:
        print 'No exception'
elif error_type == "syntax":
    try:
        print eval('five times three')
    except SyntaxError, err:
        print 'Syntax error %s (%s-%s): %s' % \
            (err.filename, err.lineno, err.offset, err.text)
        print err
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
