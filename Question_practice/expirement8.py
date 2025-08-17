#1.Add few names, one name in each row, in “name.txt file”.
#a.Count no of names
#b.Count all names starting with vowel
#c.Find longest name
'''with open('name.txt', 'r') as file:
    names = []
    for line in file:
        stripped_line = line.strip()
        if stripped_line:  
            names.append(stripped_line)
num_names = len(names)
print(f"Number of names: {num_names}")
vowels = ['A', 'E', 'I', 'O', 'U']
v = [name for name in names if name[0].upper() in vowels]
print(f"Names starting with a vowel: {len(v)}")
longest = ""
for name in names:
    if len(name) > len(longest):
        longest = name

print(f"The longest name is: {longest}")'''
#2.Store integers in a file.
#a.Find the max number
#b.Find average of all numbers
#c.count number of numbers greater than 100
'''with open("numbers.txt", 'r') as file:
    nums = [int(line.strip()) for line in file if line.strip().isdigit()]
max_num = max(nums)
average = sum(nums) / len(nums)
count_gt_100 = len([num for num in nums if num > 100])
print(f"Maximum number: {max_num}")
print(f"Average: {average:.2f}")
print(f"Count greater than 100: {count_gt_100}")'''
#3.
'''with open("city.txt", 'r') as file:
    cities = [line.strip().split() for line in file]
for city in cities:
    city[1] = float(city[1])
    city[2] = float(city[2])
print("City Details:")
for city in cities:
    print(f"City: {city[0]}, Population: {city[1]} Lakhs, Area: {city[2]} sq km")
print("\nCities with Population More than 10 Lakhs:")
for city in cities:
    if city[1] > 10:
        print(city[0])
total_area = sum(city[2] for city in cities)
print(f"\nTotal Area of All Cities: {total_area:.2f} sq km")'''
#4.
'''N = int(input("Enter number of test cases: "))
for _ in range(N):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")'''
#5.
filename = input("Enter filename to open: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except IOError as e:
    print(f"I/O Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


