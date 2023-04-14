'''
you have to fetch the data from the webpage using get request
inset the title in a list
create a search option 
result are shown according to revelance in decreasing order
'''

# practice problem
import time
import requests
import json

# defining the matching found


def matchingFound(sentences1, sentences2):

    # making a list of words from sentences
    list1 = sentences1.strip().split(" ")
    list2 = sentences2.strip().split(" ")

    # initailzing the score
    score = 0

    # matching every combination possible
    for i in list1:
        for j in list2:
            if i == j:
                score += 1

    return score


if __name__ == '__main__':

    # requesting the title for page
    data = requests.get('https://jsonplaceholder.typicode.com/posts').text
    data = json.loads(data)

    # making empty list of sentences or data
    sentences = []

    # appending all the data in the list
    for item in data:
        sentences.append(item['title'])

    # input from the user
    query = input("Enter the sentences that you want to match : ")

    # intializing the time module
    intial = time.time()

    # evualting the score according to the matches found
    scores = [matchingFound(query, sentence) for sentence in sentences]

    # zipping the sentences with there score so that it would be easy to sort them according to there indivisual score
    # a = [1,2,3]
    # b = [4,5,6]
    # d = zip(a,b) = [(1,4),(2,5),(3,6)]
    sortedSentScore = [sentence for sentence in sorted(
        zip(scores, sentences), reverse=True) if sentence[0] != 0]

    # printing the length of the sorted sentences score with time taken for completing the sorting
    print(f"{len(sortedSentScore)} Result are found in {round(time.time()-intial,3)} seounds ")

    # printing the score and senctence accoring of there decreasing oredr
    for score, sentence in sortedSentScore:
        print(f'''"{sentence}" : with a score of {score}''')
