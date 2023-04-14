with open("#31 block to open file/index.txt",encoding="utf-8") as f ,open("#31 block to open file/index1.txt","r+") as g :
    print(f.read())

    f.seek(0)
    print(f.readline(),end="")
    print(f.readline(),end="")
    print(f.readline())

    print(g.read())
    g.write("\nAdding new content")
    
    g.seek(0)
    print(g.read())

# use of block 
# Automatically closes file
# Multiple files can be opened. 
#               With open(“file1txt”) as f, open(“file2.txt”) as g