from lettuce import *

@step('I have the string "(.*)"')
def have_the_string(step, string):
    world.string = string

@step
def i_put_it_in_upper_case(step):
    world.string = world.string.upper()

@step
def see_the_string_is(step, expected):
    '''I see the string is "(.*)"'''
    assert world.string == expected, \
        "Got %s" % world.string
