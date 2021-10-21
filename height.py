import csv 

with open('heightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Removing the heading from the list
file_data.pop(0)

new_data = []

#Creating a list of only heights
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

#MEAN
n = len(new_data)
sum = 0
for j in new_data:
    sum = sum + j

mean = sum/n
print(mean)