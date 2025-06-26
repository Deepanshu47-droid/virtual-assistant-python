import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
import webbrowser
#====================================
#modules defined by me.

import Pattern_word
import Youtube_manager as ym
import tic_tac_toe
import email_validation as ev
import qr_code
import system_commands as sc
import typing_test

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'deepu' or 'dipu' in command:
                command = command.replace('deepu', '')
                command = command.replace('dipu', '')
                print(command)
            
    except:
        pass
    return command

def run_deepu():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'print pattern for' in command:
        text=command.replace('print pattern for ', '')
        Pattern_word.main(text)
    elif 'Youtube manager' in command: 
        videos = ym.load_data()
        if 'List' in command and 'videos' in command:
            ym.list_all_videos(videos)
        elif 'Add' in command: 
            ym.add_video(videos)
        elif 'Delete' in command:
            ym.delete_videos(videos)
        elif 'Update' in command: 
            ym.update_video(videos)
    elif 'tic tac toe' in command:
        tic_tac_toe.intro()
        a = tic_tac_toe.mode()
        if (tic_tac_toe.check()==1):
            tic_tac_toe.intro()
            tic_tac_toe.board()
            print(f"player {tic_tac_toe.lst[10]} won!")
            input()
        print("Thankyou! Hope you enjoyed the game.")
    elif command.startswith('repeat'):
        command=command.replace('repeat')
        talk(command)
    elif 'print' in command:
        command=command.replace('print')
        print(command)
    elif 'check email' in command:
        choice=1
        while(choice):
            ev.check_email()
            choice=int(input("Press 0 to exit. else Press any key! "))
    elif 'generate qr' in command:
        qr_code.qr_gen()
    elif 'calendar' in command:
        a=int(input("Which year calendar do you want :"))
        print(f"The calender of year {a} is : ")
        print(calendar.calendar(a,2,1,6))

    elif 'typing' in command:
        typing_test.main()
    elif 'system' in command:
        if 'restart' in command:
            sc.restart_time()
        elif 'logout' in command:
            sc.logout()
        elif 'shutdown' in command:
            sc.shutdown()

    else:
        talk('Here are the results from google. please wait')
        import webbrowser
        webbrowser.open('https://www.google.com/search?q='+command+'&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gIyCQgIECMYJxjqAjIJCAkQIxgnGOoCMgkIChAjGCcY6gIyCQgLECMYJxjqAjIJCAwQIxgnGOoCMgkIDRAjGCcY6gIyCQgOECMYJxjqAjIPCA8QLhgDGI8BGLQCGOoCMhEIEBAAGAMYQhiPARi0AhjqAjIRCBEQABgDGEIYjwEYtAIY6gIyDwgSEC4YAxiPARi0AhjqAjIRCBMQABgDGEIYjwEYtAIY6gLSAQYtMWowajeoAhSwAgE&client=ms-android-samsung-gj-rev1&sourceid=chrome-mobile&ie=UTF-8')


while True:
    run_deepu()