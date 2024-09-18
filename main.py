import pyttsx3

vtf = pyttsx3.init()

""" RATE """

rate = vtf.getProperty('rate')  # getting details of current speaking rate
vtf.setProperty('rate', 150)  # getting up new voice rate


def vtf_speak(text):
    print('speaking.....')
    print(' ')
    vtf.say(text)
    vtf.runAndWait()


txt = "Hey, I am your virtual Voice over, If you  say anything i repeat it"
vtf_speak(txt)

while txt != 'bye':
    txt = input("What should I say : ")
    print(' ')
    txt = txt.lower()
    if txt != 'bye':
        vtf_speak(txt)
    else:
        vtf_speak("See you again mate, that was nice talking to you ")
