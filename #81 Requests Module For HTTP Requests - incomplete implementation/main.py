'''
https://docs.python-requests.org/en/latest/
read the doc for more info
pip install requests

--------------x----------------------x-------------------x--------------x------------x------

requests.get(URL, params={key: value}, args)
URL: this is the URL of the website where we want to send the request. 
Params: this is a dictionary or a list of tuples used to send a query string. 
Args: It is optional. It can be any named arguments offered by the get method.
We can also fetch all the data from the homepage of a website into an HTML format using the request module. Few important types of methods defined in the request module are as follows:

requests.post(url=url, data=data)

--------------x----------------------x-------------------x--------------x------------x------

put( ):
It is used to send a put request to a variable. It is usually used to update or completely change the resources of a specific URL.

delete( ):
Delete is used to delete the specific resource specified by URL.

head( ):
The head method returns a header for a specific resource.

post( ):
Post requests take with it the data to the server to update it with.

patch( ):
The patch is used to send patch requests. It is used to apply partial modifications to a resource. It carries with it the instructions for the modification.

'''

import requests
import json

url = 'https://reqres.in/api/users'
data = requests.get(url)
print(data.text)
print(data.status_code)
parse_data = json.loads(data.text)
print(parse_data['data'])

data = {
    'name':'vishal',
    'age': 45
}
data = requests.post(url,data=data)
