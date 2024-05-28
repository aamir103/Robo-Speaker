import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Welcome To Robo Speaker Windows Version")
while True:
    x= input("Write Text to convert to Audio write stopit to stop \n")
    if x == "stopit":
        break
    speaker.Speak(x)
