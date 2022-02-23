# Importing pandas library into the program with the object name or reference as pd
import pandas as pd
# Creating a List
d = [["Sruthik", 12, 95],
     ["Bhahubali", 11, 88],
     ["kattapa", 14, 90]]
df= pd.DataFrame(d, index=[1, 2, 3], columns=["Name", "Roll Number", "Marks"])
print(df)
#Printing the second row/ record from the table created
print(df[1:2])