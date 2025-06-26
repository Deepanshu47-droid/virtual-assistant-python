letter='''Hello <|Name|> this is Python world and you are selected for the interview Please Reach in time!
Hava a great day Ahead!
Thanking you Python world
date: = <|Date|>'''

name=input("Enter Your Name\n")
date=input("Enter date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)