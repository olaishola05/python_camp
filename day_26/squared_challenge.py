numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]

result = [num for num in numbers if num % 2 == 0]

with open('file1.txt') as data_file:
    list_1 = data_file.readlines()

with open('file2.txt') as data_file_2:
    list_2 = data_file_2.readlines()

overlapping_data = [int(num) for num in list_1 if num in list_2]

print(overlapping_data)
