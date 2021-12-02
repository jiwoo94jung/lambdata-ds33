import numpy as np
class Student:

    def __init__(self, age, us_state):
        self.age = age
        self.us_state = us_state

class BloomTechStudent(Student):

    def __init__(self, age, us_state, cohort):
        super().__init__(age, us_state)
        self.cohort = cohort

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

list = []
list2 = []

def student_generator():
    for k in range(30):
        age = np.random.randint(0, 101)
        us_state = np.random.choice(states)
        cohort = np.random.randint(1,34)
        list2.append(age)
        list2.append(us_state)
        list2.append(cohort)
        list.append(list2)
    return list
print(student_generator())
