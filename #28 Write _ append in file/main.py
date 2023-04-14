f = open("#28 Write & append in file/index.txt","w",encoding="UTF-8")

f.write("this is my content 😂😅😹")

f = open("#28 Write & append in file/index.txt","a",encoding="UTF-8")
f.write("\nthis is something that is awesome 😊😅 Love python")
# If you are writing in append mode, start your text by putting a blank space or newline character (\n)

f = open("#28 Write & append in file/index.txt","r+",encoding="UTF-8")
print("one")
print(f.read())
print("two")
print(f.write("\n this is the new content that we are putting")) #it will return no to character
print(f.read())

# f.close() is used to close a file 
f.close()