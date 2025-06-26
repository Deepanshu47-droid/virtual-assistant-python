
'''
Email should have:
minimum length 6
first letter should be alphabet
only 1 @ should be in email
   '.' should be on last 3rd or 4th position
all characters should be in lowercase and there shouldn't be any space

'''

def check_email():
    email=input("Enter your Email : ")
    if len(email)>=6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@')==1):
                if (email[-4]==".")^(email[-3]=="."):
                    for i in email: 
                        if i==i.isspace(): 
                            print("wrong email! email shouldn't contain email.")
                            break
                        elif i.isalpha():
                            if i==i.upper():
                                print("wrong email! all characters should be in lowercase")
                                break
                        elif not(i.isdigit() or i=='_' or i=='.' or i=='@'):
                            print("wrong email! no symbols accepted except '_' , '.' or '@'")
                            break                    
                    else:
                        print("Email is right. ")

                else:
                    print(" wrong email '.' should be on the right position. ")
            else:
                print(" wrong email! only 1 '@' should be there.")
            
        else: 
            print(" wrong email! first character should be alphabet.")
    else:
        print(" wrong email! length should be greater than 6.")

if __name__=='__main__':
    choice=1
    while(choice):
        check_email()
        choice=int(input("Press 0 to exit. else Press any key! "))

