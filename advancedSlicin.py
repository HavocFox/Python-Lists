#Task 1: Extract the temperatures for the second week (7 days) of the month.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
sw_slice = temperatures[7:14]
print (sw_slice)

#Task 2: Extract all the temperatures above 100.

above_hundred = temperatures[23:30]
print (above_hundred)

#Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures.reverse()
five_ten = temperatures[4:10]
print(five_ten)