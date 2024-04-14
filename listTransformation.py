#Task 1: Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print('Grades are: ', grades)

#Task 2: Calculate the average grade and display it.

average = (sum(grades))/len(grades)
print('Average is: ', average)

#Task 3: Replace any grade below 80 with the value Failed.

grades.insert(7, 'Failed')
grades.insert(8, 'Failed')
grades.insert(9, 'Failed')

grades.pop()
grades.pop()
grades.pop()

print('Final grades: ', grades)