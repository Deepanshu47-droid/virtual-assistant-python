from time import *
import random as rd
import os

def speed_time(time1,time2,inp_par):
    time=time2-time1
    speed=len(inp_par.split())/time
    return str(round(speed))+" wps"

def mistake(par,inp_par):
    error=0
    for i in range(len(par)):
        try: 
            if par[i]!=inp_par[i]:
                error+=1
        except:
            error+=1

    return error

def main():
    ch='Yes'
    while ch=='Yes':
        test = [
            "There are many idiosyncratic typing styles in between novice-style \"hunt and peck\" and touch typing. For example, many \"hunt and peck\" typists have the keyboard layout memorized and are able to type while focusing their gaze on the screen. Some use just two fingers, while others use 3-6 fingers. Some use their fingers very consistently, with the same finger being used to type the same character every time, while others vary the way they use their fingers.",
            "land change small before an best would talk thing been great own same are tell story really tell song miss letter does been for every really has on look light never four four add number our great for river them seem next is high children follow best head mile other life large night no most did the most own together how hand well close earth new idea no live being these where once together even line air begin first want our together how change water add than young down set",
            "small out call go name point seem far eye large make should small let go three fire of then turn may air animal where near been why leave land word change come on every soon might life car life sea country best best story high under where like you his after fall write eye mother once at in long run did there world more many without children four man not people it about great call found long eye different because no black been two school men any best when sea",
            "between air house enough want cut form feet every move together together sun few boy does any found far night two has might side but them list cut second between different eye those life because walk make begin below as around stop plant then too world went just us back very he family she study three write feet could into light near as idea their found need sun man earth do black large mean face this call form before car go upon three letter above only house leave well make",
            "grow open without school seem spell time out fire had something say watch made men until little why add which tell when more must above much found fire new will night around mother later even is she black but world went because were he oil this food get big away man look as read oil above from thing tree or hand under form show example of which make their is close eat under there sometimes down hard water walk almost head home air around side just when children also old",
            "who those an group side got together boy off long later big help began idea think or read walk page see why children four first keep also let the always boy little second because now cut may often think enough while people found spell them group her much kind best learn must when really keep could around house we keep oil see man earth keep form set well new car many than a light country last who large on start night part near down talk put few began close country",
            "large country been went with have for almost walk until before in light at these follow part their hard world about only few any right many house line oil another great last went into being made often each face came should mother line take list him most mother very before book why near two them might country place school being then my idea fire mother paper earth more country like how ask along family got help sun each under people tree began side small were long different great face fall"]
        test1 = rd.choice(test)
        os.system('cls')
        print("******typing speed*****")
        print(test1)
        print("\n")
        time1 = time()
        testinput = input("Start typing : ")
        time2 = time()
        print("speed : ", speed_time(time1, time2, testinput))
        print("mistake : ", mistake(test1, testinput))
        ch=input('Do you want to continue : (Yes/No) ')
if __name__=='__main__':
    main()