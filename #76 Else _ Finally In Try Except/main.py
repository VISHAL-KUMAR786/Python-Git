'''
finally -> it is used to clean up , it will run in both condition weather the except had run or not

else is run when the except block was not run
'''

# x , y = [ int(x) for x in input().split(' ')]

# try:
#     n = x / y
# except Exception as e:
#     print("Exception --> ",e)
# else:
#     print("else --> it will run when the exception is not raise")
# finally:
#     print("finally --> this will run either condition")

# print('hi ')

import os 
print(os.getcwd())
f = open(r'#76 Else _ Finally In Try Except\vishal.txt','a')
# (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape 
# change the \ -> /
try:
    f1 = open('viky.txt')
except Exception as e:
    print('except -->',e)
else:
    print('else -->')
finally:
    print('finally -->')
    f.close()

print('end of the program')