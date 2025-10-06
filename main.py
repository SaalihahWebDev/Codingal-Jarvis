import datetime
import webbrowser
print("👋Hello I am BrightBuddy,your personal assistant.")
print("You can ask me things like:")
print("-Hi or Hello")
print("-🕐What time is it")
print("-📺📺📺Open Youtube")
print("-💻💻💻Open Google")
print("-💻💻💻Open Codingal")
print("-👋Bye to exit")
while True:
    command=input("You:").lower()
    if "hi" in command or "hello" in command:
        print("Brightbuddy:Hello There! How can I help you?")
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print("Brightbuddy:The current time is",time)
    elif "open youtube" in command:
        print("Brightbuddy:Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        print("Brightbuddy:Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open codingal" in command:
        print("Brightbuddy:Opening Codingal")
        webbrowser.open("https://www.codingal.com/")
    elif "bye" in command or "bye brightbuddy":
        print("Bye Bye")
    else:
        print("Brightbuddy:Sorry,I didn't understand Try something else")