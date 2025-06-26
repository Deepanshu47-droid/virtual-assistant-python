
def space(i):
    for j in range(1,3):
        print("  ",end="")

def a(i):
    for j in range(1,6):
        if i==1 or i==4 or j==1 or j==5:
            print("::",end="")
        else:
            print("  ",end="")
    space(i)

def b(i):
    for j in range(1,6):
        if i==1 or (i==3 and j!=1) or i==5 or j==2 or j==5:
            print("::",end="")
        else:
            print("  ",end="")
    space(i)
def c(i):
    for j in range(1,6):
        if j==1 or i==1 or i==5:
            print("::",end="")
        else:
            print("  ",end="")
    space(i)
def d(i):
    for j in range(1,6):
        if j==2 or j == 5 or i == 1 or i==5:
            print("::",end="")
        else:
            print("  ",end="")
    space(i)
def e(i):
    for j in range(1,6):
        if i==1 or i==3 or i==5 or j==1:
            print("::",end="")
        else:
            print("  ",end="")
    space(i)
def f(i):
    for j in range(1, 6):
        if j==1 or i==1 or (i==3 and j!=4 and j!=5):
            print("::",end="")
        else:
            print("  ",end="")
    space(i)
def g(i):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or (j==5 and i>2) or (i==3 and j>3):
            print("::",end="")
        else:
            print("  ",end="")
    space(i)


def h(i):
    for j in range(1,6):
        if i==3 or j==1 or j==5:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)


def ii(i):
    for j in range(1,6):
        if i==1 or i==5 or j==3:
            print("::",end="")
        else:
            print("  ", end="")
    space(i)


def j(i):
    for j in range(1,6):
        if i==1 or j==3 or (i==5 and j<4) or (j==1 and i>3):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def k(i):
    for j in range(1,6):
        if j==1 or i+j==5 or (i==4 and j==3) or (i==5 and j==4):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def l(i):
    for j in range(1,6):
        if i==5 or j==1:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def m(i):
    for j in range(1,6):
        if j==1 or j==5 or (i<4 and (i==j or i+j==6)):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def n(i):
    for j in range(1,6):
        if j==1 or j==5 or i==j:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def o(i):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def p(i):
    for j in range(1,6):
        if j==1 or i==1 or (i<4 and j==5) or i==3:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def q(i):
    for j in range(1,6):
        if ((j==4 or i==1 or (i<4 and j==1) or i==4) and j!=5) or (j==5 and i==5):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def r(i):
    for j in range(1,6):
        if j==1 or i+j==5 or (i==4 and j==3) or (i==5 and j==4) or (i==1 and j!=5):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def s(i):
    for j in range(1,6):
        if i==1 or i==3 or i==5 or (j==1 and i<=3) or (j==5 and i>=3):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def t(i):
    for j in range(1,6):
        if i==1 or j==3:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def u(i):
    for j in range(1,6):
        if j==1 or j==5 or i==5:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def v(i):
    for j in range(1,6):
        if j==5 or i==j:
            print("::", end="")
        else:
            print("  ", end="")
        space(i)
def w(i):
    for j in range(1,6):
        if j==1 or j==5 or ((i==j or i+j==6) and i>3):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def x(i):
    for j in range(1,6):
        if i+j==6 or i==j:
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def y(i):
    for j in range(1,6):
        if (i<=3 and (j==i or j+i==6)) or (j==3 and i>=3):
            print("::", end="")
        else:
            print("  ", end="")
    space(i)
def z(i):
    for j in range(1,6):
        if i==1 or i==5 or i+j==6:
            print("::", end="")
    else:
            print("  ", end="")
    space(i)
def main(text):

    length=len(text)
    for i in range(1, 6):
        for ch in range(length):
            if text[ch] == 'a':
                a(i)
            elif text[ch] == 'b':
                b(i)
            elif text[ch] == 'c':
                c(i)
            elif text[ch] == 'd':
                d(i)
            elif text[ch] == 'e':
                e(i)
            elif text[ch] == 'f':
                f(i)
            elif text[ch] == 'g':
                g(i)
            elif text[ch] == 'h':
                h(i)
            elif text[ch] == 'i':
                ii(i)
            elif text[ch] == 'j':
                j(i)
            elif text[ch] == 'k':
                k(i)
            elif text[ch] == 'l':
                l(i)
            elif text[ch] == 'm':
                m(i)
            elif text[ch] == 'n':
                n(i)
            elif text[ch] == 'o':
                o(i)
            elif text[ch] == 'p':
                p(i)
            elif text[ch] == 'q':
                q(i)
            elif text[ch] == 'r':
                r(i)
            elif text[ch] == 's':
                s(i)
            elif text[ch] == 't':
                t(i)
            elif text[ch] == 'u':
                u(i)
            elif text[ch] == 'v':
                v(i)
            elif text[ch] == 'w':
                w(i)
            elif text[ch] == 'x':
                x(i)
            elif text[ch] == 'y':
                y(i)
            elif text[ch] == 'z':
                z(i)
            elif text[ch] == ' ':
                space(i)
        print()
if __name__ == '__main__':
    print("created by Deepanshu Malviya.\n")
    text = input("Write something  \n")
    main(text)

