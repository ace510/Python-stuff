'''
    to run tests on mac: python3 -m doctest triathlon.py -v
    to run tests on Win: python -m doctest triathlon.py -v
'''

def triathlon(hours_cycling, hours_running, hours_swimming):
    '''
    Calculate the number of pounds lost from doing a triathlon
    based on the number of hours spent at each exercise

    given constants:
        200 calories are burned for each 1 hour of cycling
        475 calories are burned for each 1 hour of running
        275 calories are burned for each 1 hour of swimming

        a person looses 1 pound of body weight for each 3500 calories burned

    args:
        hours_cycling (float): the hours spent cycling
        hours_running (float): the hours spent running
        hours_swimming (float): the hours spent swimming

    returns:
        the number of pounds lost after the triathlon (float)

    examples/doctests:

    no cycling, running, or swimming
    >>> round(triathlon(0, 0, 0), 2)
    0.0

    1 hour cycling, no running or swimming
    >>> round(triathlon(1, 0, 0), 2)
    0.06

    no cycling, 1 hour running, no swimming
    >>> round(triathlon(0, 1, 0), 2)
    0.14

    no cycling, no running, 1 hour swimming
    >>> round(triathlon(0, 0, 1), 2)
    0.08

    5.5 hours cycling, 3.12 hours running, 2.22 hours swimming
    >>> round(triathlon(5.5, 3.12, 2.22), 2)
    0.91

    '''
    calories = (hours_cycling * 200 + hours_running * 475 + hours_swimming * 275)

    return calories / 3500
