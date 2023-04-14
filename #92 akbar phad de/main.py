'''
my api key --> 05965c30cda940f4a391569e716b4bed
https://newsapi.org/

'''
import requests 
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    time.sleep(2)

if __name__ == '__main__':
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-03-05&sortBy=publishedAt&apiKey=05965c30cda940f4a391569e716b4bed'
    data = requests.get(url) # type string
    parse_data = json.loads(data.text)
    # print(parse_data['articles'])

    # print(type(parse_data)) dict
    for i in parse_data['articles'] :
        # print(i['title'])
        speak(i['title'])