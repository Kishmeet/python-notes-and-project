import matplotlib.pyplot as plt
#LINE GRAPHS
'''x_values = [0, 1, 2, 3, 4, 5 ]
y_values = [0, 1, 4, 9, 16,25]
plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("x^2")
plt.show()
'''
#BAR GRAPHS
'''values = [5, 6, 3, 7, 2]
names  = ["A", "B", "C", "D", "E"]
plt.bar(names, values, color="green")
plt.show()

#BAR CHARTS
import matplotlib.pyplot as plt
height = [10, 24, 36, 40, 5]  
names = ['one','two','three','four','five'] 
c1 =['red', 'green']
c2 =['b', 'g']
plt.bar(names,height, width=0.8, color=c1) 
plt.xlabel('x -axis') 
plt.ylabel('y -axis') 
plt.title('My bar chart!') 
plt.show() '''
#HISTOGRAM 
'''ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40] 
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
# plotting a histogram 
plt.hist(ages, bins, range, color='green',histtype='bar',rwidth=0.8) 
plt.xlabel('age')  
plt.ylabel('No. of people') 
plt.title('Histogram') 
plt.show()'''
#SCATTER PLOT
'''x_values = [0,1,2,3,4,5]
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=30, color="red")
plt.show() 

#PIE CHARTS
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  
plt.pie(sizes, explode=explode, labels=labels, colors=colors,   autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.show()
#Plotting curves of given equations
#y = e^x
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(-5, 5, 400)
y = np.exp(x)
plt.plot(x, y, label='$e^x$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function $e^x$')
plt.grid(True)
plt.legend()
plt.show()'''

