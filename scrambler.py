'''
    Scrambler:

    A scramble is a sequence of movements to get a cube to solve.

    In this file we are going to generate an arbitrary-long scramble for any cube we want to
    get a scramble for, for which we have to set some rules:

    1- We won't support cube rotation movements.
    2- We can't repeat a movement of a layer.
    2a- In cubes bigger than the 3x3, we will allow movements of 2 or more layers at once
    (known as the 'minuscule' movements in the usual notaton), but we will not combine movements
    involving the same layers (eg, R' r2 or u2 U are not allowed).

'''

import math
import random

def get_movements(layers, movements, scramble, n):
    '''
        Recursive function, it gives a movements list
        adding a movement considering it's not repeatead.
    '''
    
    for i in range(n):
        #Loop until we have a valid layer (range from 0 to len of list)
        while True:
            layer = math.floor(10*random.random())
            if layer < len(layers):
                break
            # if layer < len(layers) and len(scramble) != 0:
            #     print(scramble[-1][0])
            #     if layers[layer] != scramble[-1][0]:
            #         break
        
        # Same with movement of the layer
        while True:
            movement = math.floor(10*random.random())
            if movement < len(movements):
                break
        
        scramble.append(f"{layers[layer]}{movements[movement]}")
    
    return ' '.join(scramble)


def scramble_2x2(n):
    '''
        Simplest cube we are going to support.

        Returns a n-long scramble for the 2x2 cube.
    '''

    layers = ('R', 'L', 'F', 'B', 'U', 'D')
    movements = ('',"'",'2')

    scramble = []

    return get_movements(layers, movements, scramble, n)


def scramble_3x3(n):
    '''
        Return a n-long scramble for the 3x3 cube.
    '''

    layers = ('R', 'L', 'F', 'B', 'U', 'D')
    movements = ('',"'",'2')

    scramble = []

    return get_movements(layers, movements, scramble, n)
