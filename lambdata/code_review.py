'''IN style_example.py FILE'''

#what would you say if you were working with someone and this is the code they gave you?
from math import pi

def exampl1():
    '''IN style_example.py FILE'''
    ### THIS IS A LONG COMMENT AND should be wrapped to fit within a 72 character limit
    some_tuple = (1,2,3,'a')
    some_variable={
        "long" : '''LONG CODE LINES should be wrapped within
        79 character to prevent page cutoff stuff''',
        "other" : [pi, 100,200, 300, 9999292929292,
                  "This IS a long string that looks gross and goes beyond what it should"],
        "more": {"inner": "THIS whole logical line should be wrapped"},
        "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]
        }
    return (some_tuple, some_variable)


def example_2():
    '''docstring'''
    return {"has_key() is deprecated": True}

class Example3:
    '''docstring'''
    def __init__(self, bar):
        self.bar = bar

    def my_method(self):
        '''docstring'''
        if self.bar:
            self.bar += 1
            self.bar = self.bar * self.bar
        else:
            some_string = """
            INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED 
            only actual code should be reindented,
            THIS IS MORE CODE
            """
        return some_string

    def my_other_method(self):
        '''docstring'''
        return self.bar * 5