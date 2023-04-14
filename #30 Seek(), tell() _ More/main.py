f = open("#30 Seek(), tell() & More/vishal.txt","r",encoding="utf-8")

print(f.readline(),end="")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

print(f.seek(0))
print(f.tell())

print(f.readline(),end="")
print(f.tell())

f = open("#30 Seek(), tell() & More/vishal.txt","rb")
print(f.seek(-10,2))
print(f.tell())
# print(f.readline().decode('utf-8'))

f.close()



# some theory

# tell()
# f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes

# seek()
# Syntax:  file_pointer .seek(offset, whence).
# Offset:   In seek() function, offset is required. Offset is the position of the read/write pointer within the file.
# default is 0

# 0: sets the reference point at the beginning of the file 
 
# 1: sets the reference point at the current file position 
 
# 2: sets the reference point at the end of the file 