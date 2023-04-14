import os

'''
print(dir(os))
It gives us a list of all the functions the OS module is composed of.

print(os.getcwd())
Here cwd is a short form for the current working directory. The function returns us the path of the directory we are currently in. It is important to know about our directory because when we are trying to import a file in python, the compiler searches for it in our current directory.

os.chdir(r'C:\Users')
It is used in case we want to change our directory. The new path is sent inside the parenthesis. If we want to access some files or folders from some other directory, we can use it.

print(os.listdir())
If we want to output the names of all the directories at a certain location, we can use this function.

print(os.mkdir('folder name'))
To create a new directory or folder. The name is sent as a parameter inside the parenthesis.

print(os.makedirs(r'/vishal')) do'nt know what it does
To make more than on directory simultaneously.

print(os.rename('source','destination'))
To rename an already existing directory, we use this. We send the current name and new name of our directory as parameters.

os.rmdir('vishal')
It deletes an empty directory.

os.removedirs('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\vishal')
We can remove all directories within a directory by using removedirs(). 

print(os.environ.get('path'))
It will return us the environment variable. The environment variable must be set, or the function will return null.

p = os.path.join('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python',
'\\vishal')
print(p)
It joins one or more path components. We can join the paths by simply using a + sign, but the benefit of using this function is that we do not have to worry about extra slashes between the components. So less accuracy still provides us with the same result.

print(os.path.exists('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\vishal'))
It returns us a Boolean value, i.e., either true or false. It is used to check whether a path exists or not. If it does, then the output will be true, otherwise false.

print(os.path.isfile('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\vishal'))     ---> false
print(os.path.isfile('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\vishal\\vk.txt'))   ---> True
It returns true if the path is an existing regular file.

os.path.splitext(file)[1]
os. path. splitext() is a built-in Python function that splits the pathname into the pair of root and ext
with '.jpg' 
'''

print(os.path.isdir('C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\vishal'))
# It returns true if the path is an existing directory.