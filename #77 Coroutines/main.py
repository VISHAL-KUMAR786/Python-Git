'''
Coroutines --> 
    it is the concept that 
        at the first it will take the time to load the file 
        but on the secound go it will start from a particular point in the function
               
Basic Syntax is :
    def myfunc():
        while True:
            value = (yield)

generator --> they generates the value of the fly
'''

def book():
    import time
    time.sleep(3)
    data = "this is my book on my personal experience"

    while(True):
        text = yield
        if text in data:
            print('Found at index 🥰-->',data.index(text))
        else:
            print('sorry not found 😭')

mycoroutines = book()
next(mycoroutines)
# next run time taking code , which is before the while 
mycoroutines.send('this')
mycoroutines.send('on')
mycoroutines.send('pp')

mycoroutines.close()
# mycoroutines.send('hi') shows the error