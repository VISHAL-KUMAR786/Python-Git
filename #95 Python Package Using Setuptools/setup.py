'''
pip install wheel
python .\setup.py bdist_wheel
python .\setup.py sdist bdist_wheel

PS C:\Users\User\Desktop\Django udemy\python basic\CWH python\#95 Python Package Using Setuptools\dist> ls
    Directory: C:\Users\User\Desktop\Django udemy\python basic\CWH python\#95 Python Package Using Setuptools\dist
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          4/6/2022   5:00 PM           5487 this-0.1-py3-none-any.whl
-a----          4/6/2022   5:00 PM           5449 this-0.1.tar.gz

pip install .\this-0.1.tar.gz
Import package_name

-----------------x-------------------------x---------------------x---------------------x-------------------
name: The name of the package. We can give our package any name of our choice.

version: The starting version should be 0.1 because, with any update, it automatically increases it to one decimal place.

description: Here, we give a brief description of our package and its functionalities and uses.

long_description: In the long description we give an explanatory description of our package

author: We can specify the creator of the package here

packages: Here we give the name by which we want our package to be called or imported

install_requires: If our package has a prerequisite package, then we have to specify that here so both of them can work simultaneously and can perform better.

'''
from setuptools import setup

setup(
    name="this",
    version=0.01,
    description="This is my description about my cli app in python",long_description="this is my long edescription about the cli app in pyhton",
    author="vishal kumar",
    packages=['vishalApp'],
    install_requires=[]
)

# setup(name="this",version=0.01,description="This is my description about my cli app in python",long_description="this is my long edescription about the cli app in pyhton",author="vishal kumar",author_email="xxxx--xx@gmail.com",maintainer="This thing is maintained by vishal kumar",maintainer_email="maintainer-xxx@gmail.com",url="https://youtube.com",)