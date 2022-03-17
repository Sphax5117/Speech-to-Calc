import requests
import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

word = input("What is your word ? ")
url = "https://wordsapiv1.p.rapidapi.com/words/" + word +"/antonyms"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "a7e6fada6dmsh3df24a8d9730036p162da1jsn3620a50496b1"
    }

response = requests.request("GET", url, headers=headers)
data = response.json()

print("The antonym of " + ''.join(data["word"]) + " is " + ' or '.join(data["antonyms"]))
