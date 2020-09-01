"""
    to run tests on mac: python3 -m doctest cost_of_running_lightbulb.py -v
    to run tests on Win: python -m doctest cost_of_running_lightbulb.py -v
"""


def cost_of_running_lightbulb(cents_per_kw_hour, bulb_wattage, hours_on):
    """
    Calculate the cost of running a lightbulb using the formula
    wattage x hours used divided by 1000 x cost per kWh in cents

    args:
        cents_per_kw_hour (float): the cost in cents per kilowatt hour
        bulb_wattage (float): the wattage of the bulb
        hours_on (float): the number of hours the bulb was on

    returns:
        the cost of running the lighbulb in dollars

    examples/doctests:

    1 penny per kw hour, 60 watt bulb, zero hours on
    >>> round(cost_of_running_lightbulb(1, 60, 0), 2)
    0.0

    $0.10 per kw hour, 100 watt bulb, 1 hour on
    >>> round(cost_of_running_lightbulb(10, 100, 1), 2)
    0.01

    $0.10 per kw hour, 100 watt bulb, 100 hours on
    >>> round(cost_of_running_lightbulb(10, 100, 100), 2)
    1.0

    $0.15 per kw hour, 60 watt bulb, 25 hours on
    >>> round(cost_of_running_lightbulb(15, 60, 25), 2)
    0.1

    $11.76 per kw hour, 127 watt bulb, 56789 hours on
    >>> round(cost_of_running_lightbulb(1176, 127, 56789), 2)
    6.13

    """
    grundle = (bulb_wattage * hours_on) / (1000 * cents_per_kw_hour)
    return grundle
