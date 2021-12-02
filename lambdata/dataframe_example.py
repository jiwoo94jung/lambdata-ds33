import pandas as pd

# object = Class Constructor
# an object once it has been created is called an "instance"
# The act of creating an object from a class constructor is called "instantiation"

# one instance of a dataframe object created from the class constructor
df = pd.DataFrame({'a': [1,2,3] , 'b': [4,5,6]})

# a second instance of a dataframe object created from the class constructor
df1 = pd.DataFrame({'a': [1,2,3] , 'b': [4,5,6]})

# a third instance of a dataframe object created from the class constructor
df2 = pd.DataFrame({'a': [1,2,3] , 'b': [4,5,6]})

# Class variables are called "attributes"
# attributes do not have parentheses
print(df.shape) # -> (3,2)
print(df.index)
print(df.dtypes)

# Class functions are "methods"
# methods have parentheses
#print(df.drop())
print(df.describe())
print(df.head())

#from sklearn.linear_model import LinearRegression

#model = LinearRegression()

#model.fit()

#from sklearn.metrics import mean_absolute_error

#mae = mean_absolute_error()