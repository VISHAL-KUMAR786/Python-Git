'''
uci ml(machine learning) > data set > irs
https://archive.ics.uci.edu/ml/datasets/Iris 
'''

import pickle
import requests 

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

data = requests.get(url).text
data = data.split('\n')

data = [ item.split(',') for item in data if len(item)!=0] 

with open(r'D:\IMP DOCUMENT\vishal\CWH python\#85 Pickling Iris -inc\vishal.txt', 'wb') as f:
    pickle.dump(data,f)

with open(r'D:\IMP DOCUMENT\vishal\CWH python\#85 Pickling Iris -inc\vishal.txt', 'rb') as f:
    print(pickle.load(f))