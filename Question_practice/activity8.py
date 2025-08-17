'''#1.How do you open a file in Python, and what are the different modes you can use?
# To open a file in Python, we use the `open`
#function which takes at least the name of the file,
#and optionally the mode to open the file with.
with open("file.txt", "r") as file:
    content = file.read()

with open("file.txt", "a") as file:
    file.write(content)

with open("file.txt", "w") as file:
    file.write(content)

with open("file.txt", "rb") as file:
    content = file.read()

with open("file.txt", "ab") as file:
    file.write(content)

with open("file.txt", "wb") as file:
    file.write(content)

with open("file.txt", "r+") as file:
    content = file.read()

with open("file.txt", "a+") as file:
    file.write(content)

with open("file.txt", "w+") as file:
    file.write(content)

with open("file.txt", "rb+") as file:
    content = file.read()

with open("file.txt", "ab+") as file:
    file.write(content)

with open("file.txt", "wb+") as file:
    file.write(content)

#2.How do you read the contents of a file in Python?
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()
#3.How do you write to a file in Python?
file = open("text.txt", "w")
file.write("Hello, world!\nThis is a new file.")
file.close()
file = open("text.txt", "r")
content = file.read()
print(content)
file.close()

#4.How do you append to an existing file in Python?
file = open("text.txt", "a")
file.write("\nAppending this new line.")
file.close()


#5.How do you close a file in Python, and why is it important to do so?
file = open("text.txt", "r")
content = file.read()
print(content)
file.close()

1. Releases System Resources – Frees up memory and file handles allocated by the OS.
2. Prevents Data Loss – Ensures all buffered data is written to the file.
3. Avoids File Corruption – Reduces the risk of incomplete or corrupted files in case of crashes.
4. Prevents "Too Many Open Files" Error – Avoids exceeding system limits on open files.
5. Allows Other Programs to Access the File – Some OS lock files while they are open.
6. Improves Code Maintainability – Helps in debugging and prevents hidden issues.
7. Use with Statement for Auto-closing – Ensures the file is closed automatically. 



#6.How do you use the with clause to open and read a file in Python?
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
  
#7.How do you use the with clause to write to a file in Python?
with open("abc.txt", "w") as file:
    file.write("The file name is abc")


#8.Write a program that reads a file line by line using readline(), counts the number of lines, and prints the total number of lines at the end.
with open("myfile.txt", "r") as file:
        line_count = 0
        while True:
            line = file.readline()
            if not line:
                break
            line_count += 1
        print(f"Total number of lines: {line_count}")

#9.Write a program that reads a file into a list of strings using readlines(), removes any whitespace characters
#from the beginning and end of each line, and writes the modified lines back to the file using writelines().
with open("string.txt", "r") as file:
    L=file.readlines()
    a=[l.strip()+"\n" for l in L]
with open("string.txt", "w") as file:
    file.writelines(a)

#10.Write a program that reads a binary file into a byte string, seeks to the middle of the file,
#and writes the byte string from that point on to a new file.
with open("binary.bin.txt", "rb") as input_file:
        file_size =input_file.read()
        middle_point = len(file_size) // 2  
        input_file.seek(middle_point)
        byte_string = input_file.read()
with open("newfile.txt", "wb") as output_file:
        output_file.write(byte_string)
print(f"Successfully written the byte string from the middle of binary.bin.txt to newfile.txt.")
#11.Write a program that reads a file into a byte string, seeks to the end of the file, and writes the byte string backwards to a new file.
with open("file.txt","rb+") as infile,open("file2.txt","wb") as outfile:
    bstring=infile.read()
    print(bstring)
    bstring=bstring[::-1]
    print(bstring)
    outfile.write(bstring)

#12.Write a program that reads a file into a byte string, seeks to the middle of the file,
#and overwrites the byte string from that point on with a different byte string of the same length.
with open("file.txt","rb+") as file:
    file_content = file.read()
    mid=len(file_content)//2
    content=file_content[mid ::-1]
    print(len(file_content)-mid,len(content))
    if len(content)!=len(file_content)-mid:
        raise ValueError("The new data must be the same length as the remaining content from the middle.")
    file.seek(mid)
    file.write(content)
#13.Write a Python program that reads a file and sorts the words in alphabetical order.
with open ("file.txt","r") as file:
    words=file.read().split()
    words.sort()
with open("sortedfile.txt","w") as file:
    file.write(" ".join(words))


#14.Write a Python program that reads a file and removes all the punctuation marks from the text.
import string
with open("punctuation.txt", 'r') as file:
    content = file.read()
    punctuation = set(string.punctuation)
    clean_content = ''.join(char for char in content if char not in punctuation)
    print(clean_content)
with open('cleaned.txt' , 'w') as file:
        file.write(clean_content)
#15.Write a Python program that reads a file and prints the 10 most common words in it, along with their frequency.
with open("freq.txt", 'r') as file:
    content = file.read()
    content = content.lower()
    word_counts = {}
    word = ''
    for char in content:
        if char.isalnum():
            word += char
        else:
            # If we hit a non-alphanumeric character, it indicates the end of a word
            if word:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
                word = ''  # Reset the word for the next one 
    # If the last word ends without punctuation, we need to add it to the dictionary
    if word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    top_words = []
    for i in range(10):
        # Find the word with the maximum frequency
        max_word = None
        max_freq = 0
        for word, freq in word_counts.items():
            if freq > max_freq:
                max_freq = freq
                max_word = word
        top_words.append((max_word, max_freq))
        
        # Remove the word from the dictionary so it won't be counted again
        if max_word in word_counts:
         del word_counts[max_word]
    for word, freq in top_words:
        if word==None and freq==0:
            break
        print(f'{word}: {freq}')   
'''

#16.Write a Python program that reads a file and replaces all occurrences of a word with another word.
#The program should prompt the user for the word to be replaced and the new word.    
with open("freq.txt", 'r') as file:        
     content = file.read()
     rword=input("Enter word to replace: ")
     nword=input("Enter new word: ")
     content=content.replace(rword,nword)
with open("freq.txt", 'w') as file:
    file.write(content)
     
