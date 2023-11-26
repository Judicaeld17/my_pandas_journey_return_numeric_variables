# TASK: Create a function which receive a pandas dataframe as parameter and returns the corresponding numeric variables.
import pandas as pd
import numpy as np
def my_pandas_journey_return_numeric_variables(df):
   return df.select_dtypes(include=np.number) 
