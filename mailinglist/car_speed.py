import math

'''
    to run tests on mac: python3 -m doctest car_speed.py -v
    to run tests on Win: python -m doctest car_speed.py -v
'''

def car_speed(distance_of_skid):
    '''
    Calculate the speed in MPH of a car that skidded
    d feet on dry concrete when the brakes were applied

    args:
        distance_of_skid (float): the distance of the skid in feet

    returns:
        an estimate of the speed the car was going when the brakes were applied (float)

    formula:
        speed in MPH equals the square root of (24 * d)

    examples/doctest:

    the car didn't skid at all
    >>> round(car_speed(0), 2)
    0.0

    the car skid 1 foot
    >>> round(car_speed(1), 2)
    4.9

    the car skid 10 feet
    >>> round(car_speed(10), 2)
    15.49

    the car skid 33.33 feet
    >>> round(car_speed(33.33), 2)
    28.28

    the car skid 12345 feet
    >>> round(car_speed(12345), 2)
    544.32

    '''
    skid_float = float(distance_of_skid)
    mph = math.sqrt(skid_float * 24)
    
    return mph
