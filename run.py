import autopy
import math
import time
import random
import sys
from svg.path import parse_path
import numpy as np
import subprocess

# TODO
# Start at current point (retrieve current position) and set to basis
# Differeniate between Line (faster) and Move (move manually)
# You can retrieve color from screen 
# Shortcut for canceling
# Shortcut for starting with link from clipboard

# define the function blocks
def handle_move(segment):
    #autopy.mouse.move(segment.end.real,segment.end.imag)
    print("handle move to " + str(segment.end.real) +"||" + str(segment.end.imag))

def handle_line(segment):
    #autopy.mouse.move(segment.start.real,segment.start.imag)
    #autopy.mouse.toggle(down=True, button=autopy.mouse.Button.LEFT)
    #autopy.mouse.smooth_move(segment.end.real,segment.end.imag)
    #autopy.mouse.toggle(down=False, button=autopy.mouse.Button.LEFT)
    print("handle line for start: " + str(segment.start) + " and end: "+ str(segment.end))

def sample_geometry(segment, basis):
    for x in np.arange(0, 1, 0.1):
        autopy.mouse.toggle(down=True, button=autopy.mouse.Button.LEFT)
        point = segment.point(x)
        #autopy.mouse.move(point.real,point.imag)
        autopy.mouse.smooth_move((point.real/1)+basis,(point.imag/1)+basis)
        autopy.mouse.toggle(down=False, button=autopy.mouse.Button.LEFT)

def parse_geometry():
    result = subprocess.run(['bash', 'convert.sh', 'child.jpg'], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8") 

# map the inputs to the function blocks
options = {"Move" : handle_move,
           "Line" : handle_line,
}


def hello_world():
    paths = parse_geometry().splitlines()
    basis = 300
    for path in paths:
        for segment in parse_path(path):
            #options[segment.__class__.__name__](segment)
            #autopy.mouse.move(segment.start.real,segment.start.imag)
            sample_geometry(segment, basis)
        autopy.mouse.click()
hello_world()
