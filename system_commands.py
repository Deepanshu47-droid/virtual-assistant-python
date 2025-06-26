import os 

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t "+input("Enter seconds. "))
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

if __name__=='__main__':
    while True: 
        print(""""
Press 1 for restart. 
Press 2 for restart with time. 
Press 3 for logout. 
Press 4 for shutdown.
Press 0 for exit.  """)
        choice=input()
        match choice:
            case '1':
                restart()
            case '2':
                restart_time()
            case '3':
                logout()
            case '4':
                shutdown()
            case _:
                print("invalid input!")