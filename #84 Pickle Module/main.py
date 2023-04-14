'''
Pickle means to preserve ::: it is consider a security concern

two types 
    1. Pickling
    2. Unpickling

Pickling is the process of serializing an object. Serializing means storing the object in the form of binary representation so it can be saved in our main memory

we have to make a file with the .pkl extension and send it in a dump() function along with the object. dump() is a built-in function in the Pickle module, made for pickling.
'''

import pickle

data ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

# with open(r'D:\IMP DOCUMENT\vishal\CWH python\#84 Pickle Module\data.pkl',"wb") as f :
#     pickle.dump(data,f)

with open(r'D:\IMP DOCUMENT\vishal\CWH python\#84 Pickle Module\data.pkl','rb') as f:
    data = pickle.load(f)
    print(data)

