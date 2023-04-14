'''
what are the different types of license 

    1.  Public domain. This is the most permissive type of software license. When software is in the public domain, anyone can modify and use the software without any restrictions. But you should always make sure it’s secure before adding it to your own codebase. Warning: Code that doesn’t have an explicit license is NOT automatically in the public domain. This includes code snippets you find on the internet.

    2. Permissive. Permissive licenses are also known as “Apache style” or “BSD style.” They contain minimal requirements about how the software can be modified or redistributed. This type of software license is perhaps the most popular license used with free and open source software. Aside from the Apache License and the BSD License, another common variant is the MIT License.

    3.  LGPL. The GNU Lesser General Public License allows you to link to open source libraries in your software. If you simply compile or link an LGPL-licensed library with your own code, you can release your application under any license you want, even a proprietary license. But if you modify the library or copy parts of it into your code, you’ll have to release your application under similar terms as the LGPL.

    4.  Copyleft. Copyleft licenses are also known as reciprocal licenses or restrictive licenses. The most well-known example of a copyleft or reciprocal license is the GPL. These licenses allow you to modify the licensed code and distribute new works based on it, as long as you distribute any new works or adaptations under the same software license. For example, a component’s license might say the work is free to use and distribute for personal use only. So any derivative you create would also be limited to personal use only. (A derivative is any new software you develop that contains the component.)
    The catch here is that the users of your software would also have the right to modify the code. Therefore, you’d have to make your own source code available. But of course, exposing your source code may not be in your best interests.

    5.  Proprietary. Of all types of software licenses, this is the most restrictive. The idea behind it is that all rights are reserved. It’s generally used for proprietary software where the work may not be modified or redistributed.

what is the Structure of License
    SUPPORT                                            
    LICENSE SUMMARY  
    LEGAL           
    QUICK START INSTRUCTIONS 
    LICENSE KEYS START HERE
    LICENSE END

----------------------x-----------------------x------------------------x---------------x--------------------

for more on readme.md file
    https://www.mygreatlearning.com/blog/readme-file/

Basic Structure of Readme file
    Project Title   
    Motivation
    Build Status
    Code Style
    Screenshots
    Tech/Framework used
    Features
    Code Examples
    Installation
    API reference
    Tests
    How to Use?
    Contribute
    Credits
    License
'''
class AddingTwo:

    def __init__(self , len , bre) -> None:
        self.len = len
        self.bre = bre
    
    def __add__(self,other):
        return f"length is {self.len + other.len} & breadth is {self.bre + other.len}"
    # these are dunder method in python