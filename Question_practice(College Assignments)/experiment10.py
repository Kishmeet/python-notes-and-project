#Experiment 10: Data Analysis and Visualization 
#1.Create numpy array to find sum of all elements in an array.
'''import numpy as np
array = np.array([x for x in range(1,int(input("Enter the number of elements in the array: "))+1)]),
array_sum = np.sum(array)
print("The sum of all elements in the array is:", array_sum)'''
#2.Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
'''import numpy as np

array = np.array([[3, 5, 7],
                  [2, 8, 6],
                  [4, 1, 9]])

row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
flattened_array = array.flatten()
second_max = np.sort(flattened_array)[-2]

print("Original Array:")
print(array)

print("\nSum of each row:")
for i, row_sum in enumerate(row_sums, start=1):
    print(f"Row {i}: {row_sum}")

print("\nSum of each column:")
for i, column_sum in enumerate(column_sums, start=1):
    print(f"Column {i}: {column_sum}")

print("\nSecond maximum element in the array:", second_max)'''
#3.Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array.
'''import numpy as np
n = int(input("\nEnter the size of the square matrices (n x n): "))
print("\nEnter elements for Matrix 1:")
matrix1 = np.array([list(map(int, input().split())) for _ in range(n)])
print("\nEnter elements for Matrix 2:")
matrix2 = np.array([list(map(int, input().split())) for _ in range(n)])
    
result = np.dot(matrix1, matrix2)

print("\nMatrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of Matrix Multiplication:")
print(result)'''
#4.	 Write a Pandas program to get the powers of an array values element-wise. 
#Note: First array elements raised to powers from second array
'''import pandas as pd
print("Enter values for the first DataFrame (space-separated, row by row):")
rows1 = int(input("Number of rows: "))
data1 = {}
for i in range(rows1):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    data1[f"Col{i + 1}"] = row
print("\nEnter values for the second DataFrame (space-separated, row by row):")
rows2 = rows1  # Ensure the same number of rows
data2 = {}
for i in range(rows2):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    data2[f"Col{i + 1}"] = row
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
result = df1 ** df2
print("\nFirst DataFrame:")
print(df1)

print("\nSecond DataFrame:")
print(df2)

print("\nResult of Element-wise Powers:")
print(result)'''
#5.Write a Pandas program to get the first 3 rows of a given DataFrame.
'''import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

first_three_rows = df.head(3)
print("First three rows of the DataFrame:")
print(first_three_rows)'''
# 6. Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
'''import pandas as pd
import numpy as np

rows = int(input("Enter the number of rows: "))
columns = input("Enter the column names (comma-separated): ").split(',')

data = {}
for col in columns:
    print(f"Enter values for column '{col}' (use 'nan' for missing values, space-separated):")
    data[col] = [float(x) if x != 'nan' else np.nan for x in input().split()]

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

replace_value = float(input("\nEnter the value to replace missing values: "))
df.fillna(replace_value, inplace=True)

print("\nDataFrame after replacing missing values:")
print(df)'''
#7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100) 
y1 = np.tan(x)  
y2 = x**2
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Line Plot for tan(x)
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(np.linspace(0.1, 10, 100) , y1, label='tan(x)', color='blue')
plt.axhline(y=0, color='black', linestyle='--')
plt.title('Line Plot for tan(x)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.ylim(-10, 10)

# Bar Plot
plt.subplot(2, 2, 2)
plt.bar(categories, values, color='green')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Scatter Plot for x^2
plt.subplot(2, 2, 3)
plt.scatter(x, y2, color='purple', label='x^2', alpha=0.7, edgecolor='black')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
plt.title('Scatter Plot for x^2', fontsize=12)
plt.xlabel('x-axis', fontsize=10)
plt.ylabel('y-axis', fontsize=10)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend()


# Pie Chart
plt.subplot(2, 2, 4)
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['blue', 'red', 'green', 'yellow'])
plt.title('Pie Chart')

# Show all plots
plt.tight_layout()
plt.show()
