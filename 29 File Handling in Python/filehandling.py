#Writing content in file
'''
.write("content")
.writelines(lines)#write multiple lines
'''
#'w' write the conent on file (overrites if exists)
with open("sample.txt","w") as file:
    file.write("Hello everyone to my channel\n")
    file.write("Lets write some code...")
    print("done writing...")


#.writelines(lines)
lines = ["line 1:This is line one","line 2:This is line two","line 3:This is line three","line 4:This is line four",]
with open("sample.txt","a") as file:
    file.writelines(lines)
    print("written multiple lines......")


#'a' => append at last line
with open("sample.txt", "a") as file:
    file.write("now I am append some line of code...")



#--------------CREATE NEW FILE AND ADDED CONTENT--------
#Create a new file
# 'x' mode => error if exists
try:
    with open("demo.txt",'x') as file:
        file.write("I have created new file and added some content")
        print("done creating new file and added content!")
except FileExistsError:
    print("File name already exists!!!")
    

#---------Read Entair File---------------
#.read()
#.readline()
#.readlines()

#.read()
with open("sample.txt",'r') as file:
    content = file.read()
    print("readed content: ",content)

#.readline(): read only this single line
with open("sample.txt",'r') as file:
    content = file.readline()
    print("reading single line: ",content)

#.readlines(): read multiple lines(it read as an list)
with open("sample.txt",'r') as file:
    content = file.readlines()
    print("readed content: ", content)  
    
#------------Read and Write together--------
#w+(write and read)
with open("sample2.txt",'w+') as file:
    file.write("This is my linessss friendss....\n hope you ding file")
    file.seek(0)#read from 0  charecter
    content = file.read()
    print(">>>>>>>>>>>>",content)

#r+(read and write)
with open("sample2.txt",'r+') as file:
    content = file.read()
    file.seek(0)
    file.write("I AM WRITING SOME CODEEEEE")
    content = file.read()
    print("#######",content)


#PROFESSINAL WAY(FileNotFoundError, FileExistsError)
try:
    with open("nonexistingfile.txt",'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File Not Found!!!")
    
    
#FileExistsError
try:
    # Trying to create a file that already exists
    with open("demo.txt", 'x') as f:
        f.write("Hello, World!")
except FileExistsError:
    print("File already exists!")
