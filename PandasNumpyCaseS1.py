#1 Extract data from the givenSalaryGender CSV fileand store the data from each column in 
#a separate NumPy array
import numpy as np
import csv as cs
import pandas as pd
print("\n\nQ(1):\n")

import numpy as np
import pandas as pd

df_salary_gender = pd.read_csv("files/SalaryGender.csv")

salary = np.array(df_salary_gender["Salary"])
gender = np.array(df_salary_gender["Gender"])
age = np.array(df_salary_gender["Age"])
phd = np.array(df_salary_gender["PhD"])
print(salary, gender, age, phd)         


#2.Find:1. The number of men with a PhD2. The number of women with a PhD

import numpy as np
import pandas as pd

df_salary_gender = pd.read_csv("files/SalaryGender.csv")

mens_phd = df_salary_gender.query("Gender == 1 and PhD == 1")
women_phd = df_salary_gender.query("Gender ==1 and PhD ==1")

print("The number of men with a PhD " + str(len(mens_phd)))
print("The number of women with a PhD" + str(len(women_phd)) )


#3.Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhDfrom SalaryGender CSV file.

import pandas as pd

csv_data = pd.read_csv('files/SalaryGender.csv')

# filter columns
age_phd = csv_data.filter(["Age", "PhD"])

people_phd =age_phd.drop(age_phd[age_phd["PhD"] == 0].index)

print(people_phd)

# 4.Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.
import pandas as pd

csv_data = pd.read_csv('files/SalaryGender.csv')

employee_phd=csv_data.query("PhD == 1")
print("Total number of people with PhD degree" + str(len(employee_phd)))


#5.How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of Integers?

input_array = [0, 5, 6, 0, 4, 4, 3, 3, 0, 5, 2, 1, 1, 9]

count_each_element=[input_array.count(item)for item in set(input_array)]
print(count_each_element)


#6 Create a numpy array [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements greater than 5.Min value
import numpy as np

np_input_array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
arr_gt_5 = np_input_array[np_input_array > 5]

print(arr_gt_5)

#7.Create a numpy array having NaN (Not a Number) and print it.array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])Print the same array omitting all elements which are nan

import numpy as np

np_array_input = np.array([np.NaN,   1.5,   2.8,  np.NaN,   3.,   4.,   5.])
print(np_array_input)

arr_without_nan = np_array_input[~np.isnan(np_array_input)]  # use ~ for negation
print(arr_without_nan)

#8 Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values

import numpy as np

np_input_arry =np.random.random((10,10))
print(np_input_arry)

print("Max value " + str(np_input_arry.max()))
print("Min value " + str(np_input_arry.min()))

#9 Create a random vector of size 30 and find the mean value.
import numpy as np
import random

Z = np.random.random(30)
x, y = 0, 0

while x*y != 30:
     x = random.randint(1, 31)
     y = random.randint(1, 31)

Z = Z.reshape(x, y)

print(Z)
mean_Z = Z.mean()
print("Mean calculated as "+str( mean_Z))
#10 Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
import numpy as np

np_array = np.arange(0, 10)
np_array = [(-d if (d > 3 and d < 9) else d) for d in np_array]

print(np_array)

#11.Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 
#2ndcolumn or 3rdcolumn.

import numpy as np

np_array = np.random.random(9).reshape(3, 3)
print(np_array)

np_new_sorted = np.sort(np_array, axis=0)
print("Sorted array as follows :")
print(np_new_sorted)

#12.Create a four dimensions array get sum over the last two axis at once.
import numpy as np
from numpy import random

a=np.array(np.random.randn(2,2,2,2))
print(a)
print(" last 2 axis at once :")
print(a[1:])
print("Sum of last 2 axis at once :")
print(a[1:].sum())
import numpy as np

np_array = np.random.random(16).reshape(2, 2, 2, 2)
print(np_array)
np.sum(np_array, axis=0)


#13.Create a random array and swap two rows of an array.
import numpy as np
 
num_arr = np.array([[1,3,1], [3,1,3], [2,9,2], [9,2,9]])
 
# Displaying the original array
print("Original array:")
print(num_arr)
 
# Using np.roll() method for swapping array along row
num_arr = np.roll(num_arr,2,axis=0)
 
print("\nArray after swapping the rows:")
print(num_arr)
#14.Create a random matrix and Compute a matrix rank
import numpy as np

np_array = np.random.random(16).reshape(2, 2, 2, 2)
print(np_array)

array = np.array([4, 2, 7,  1])
temp = array.argsort()
ranks = np.empty_like(temp)
ranks[temp] = np.arange(len(array))
print(ranks)

#15 Phase 1 -Data Collection
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

df_school_data = pd.read_csv('middle_tn_schools.csv')
#print(df_school_data.head())
#df_school_data.describe()

# 15 Phase 2 
df_grouped_data = df_school_data.groupby("school_rating").describe()
print(df_grouped_data.head())
# 15 Phase3 Phase 3 –Correlation analysisFind
corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

# Phase 4 –Scatter PlotFind the relationship
plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()

