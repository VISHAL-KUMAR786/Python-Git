'''
for some more regex topics refer to
https://docs.python.org/3/library/re.html


findall: It finds all searches for matches and prints resultant in the form of a list.

search: It works the same as a findall, but the resultant is a matched object if any is found.

split: The split function splits the string from every matched into two new strings.

sub: The sub-function works exactly like a replace function in notepad or MS Word. It replaces the original word with a word of our choice.

finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object. So, most of the examples we are going to see next will contain a finditer function in them.
'''


import re

mystr = '''Tata Limited Dr. David Landsman, executive director 18, Grosvenor Place London SW1X 7HSc Phone:  +44 (20) 7235 8281 Fax: +44 (20) 7235 8727 Email: tata@tata.co.uk Website: www.europe.tata.com Directions: View map 
Tata Sons, North America 1700 North Moore St, Suite 1520 Arlington, VA 22209-1911 USA Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791 66-66 455-4545 Email: northamerica@tata.com Website: www.northamerica.tata.com Directions: View map fass harry bhai lekin bahut hi badia aa00dmi haiaiinaiiiiiiiiiiii'''

# myPattern = re.compile(r'.iew')
# myPattern = re.compile(r'^Tata')
# myPattern = re.compile(r'ii$')
# myPattern = re.compile(r'27*')
# myPattern = re.compile(r'ai*')
# myPattern = re.compile(r'ai+')
# myPattern = re.compile(r'ai{2}')
# myPattern = re.compile(r'vi*|ai*')
# myPattern = re.compile(r'(sm){1}')
# myPattern = re.compile(r'(ta){1}')
# myPattern = re.compile(r'\ATata')
# myPattern = re.compile(r'\bhaiaiinaiiiiiiiiiiii\b')
# myPattern = re.compile(r'\bhaiaiinaiiiiiiiiiiii')
# myPattern = re.compile(r'haiaiinaiiiiiiiiiiii\b')
# myPattern = re.compile(r'\Bad')
# myPattern = re.compile(r'\d{5}-\d{4}')
# myPattern = re.compile(r'a*\D')
# myPattern = re.compile(r'\Sa')
# myPattern = re.compile(r'aa\w')
# myPattern = re.compile(r'a\w')
# myPattern = re.compile(r'\W{1}')
myPattern = re.compile(r'aiiiiiiiiiiii\Z')

l1 = myPattern.finditer(mystr)

# print(mystr[203:207])
# print(mystr[439:443])
# print(mystr[485:495])

for i in l1:
    print(i)





