#  ye script aapko latest news headlines padh ke sunaye gi 
import pyttsx3
import requests
import json

def speaker(no,newnews):
    engine = pyttsx3.init()
        #getting details of current voice
    voices = engine.getProperty('voices') 
        #changing index, changes voices. 1 for female
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    # rate = engine.getProperty('rate')
    engine.setProperty('rate', 110)
    engine.setProperty('voice', voices[2].id ) 
    print("-"*50)
    print(f"news {no} : {newnews}")
    engine.say(f"news {no}")
    engine.say(newnews)
    engine.runAndWait()
    engine.stop()



if __name__ == "__main__":
    tokken = input("Enter your news api tokken/key: ")
    code = input("Enter iso code of your country: ")
    url = f"https://newsapi.org/v2/top-headlines?country={code}&apiKey={tokken}"
    response = requests.get(url)
    titles = response.json()
    newtitles = titles["articles"]
    count = 1

    print("="*50)
    print("         TOP HEADLINES        ")
    for x in newtitles:
        newnews = x["title"]
        speaker(str(count), newnews)
        count += 1
    print("="*50)
