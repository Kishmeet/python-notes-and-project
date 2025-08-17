#1.Add few names, one name in each row, in “name.txt file”.
#a.Count no of names
#b.Count all names starting with vowel
#c.Find longest name

with open('name.txt', 'r') as file:
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

print(f"The longest name is: {longest}")
