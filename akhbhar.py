#  my api key is 6f85e6bc012a4f779919bb0d60661289

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
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=6f85e6bc012a4f779919bb0d60661289')
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
