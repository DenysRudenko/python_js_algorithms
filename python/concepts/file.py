import os
print(os.getcwd())

# my_file = open('concepts/txt/myfile.txt')

# suing read() function to open print out the info in documents
# print(my_file.read())

# resets the cursor to begging
# my_file.seek(0)

# print(my_file.read())

# my_file.seek(0)

# print(my_file.readlines())

# my_file.close()

#  mode='r'     => is read only
#  mode ='w'   => is write only
#  mode ='a'   => is append only
#  mode ='r+'  => is reading and writing 
#  mode = 'w+' => is writing and reading (Overwrites the existing file)

with open('concepts/txt/myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# mode = w means write
with open('concepts/txt/myfile.txt', mode='a') as my_append_file:
    my_append_file.write('\nthis is fourth line')


# mode = r means read
with open('concepts/txt/myfile.txt', mode='r') as my_other_file:
    content = my_other_file.read()
    print(content)

with open('concepts/txt/my_new_file.txt', mode='w') as my_other_file:
    content = my_other_file.write('This is file created by python')

    # counts the chars i wrote in my file
    print(content)

# creates a new test.txt file, writes some info and close it
with open('concepts/txt/test.txt', mode='w+') as new_test_file:
    new_test_file.write("new line i created using python")
    new_test_file.seek(0)

    content = new_test_file.read()

    print(content)