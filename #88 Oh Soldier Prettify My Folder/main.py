'''
def soldier("C://", "harry.txt", "jpg")
The function will perform three tasks:

First, it will check all the files present in the folder whose paths are given as an input argument.
Then it will capitalize the first letter of each file. If the file's name is present in a dictionary file, then it will not capitalize the first letter. It will only capitalize the first letter of the files, which are not present in the dictionary file. 
The function renames the file names to numbers in the range of 1 to100 whose format is the same as mentioned in the input parameter like 1.jpg.
'''
import os
def soldier(path,file,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

if __name__ == '__main__':
    path = "C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\#80 Oh Soldier Prettify My Folder\\vishal"
    file ="vk.txt"
    extension = ".jpg"
    soldier(path,file,extension)
