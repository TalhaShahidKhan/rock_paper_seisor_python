#Rock Paper Scissor game with PYTHON
import pyttsx3
import random

You=input("You::Enter rock(r), paper(p) or scissor(s):")


#gamewin function:
def gamewin(p1,comp):
    if p1==comp:
        return None
    elif p1=='r':
        if comp=='p':
            return True
        elif comp=='s':
            return False
    elif p1=='p':
        if comp=='r':
            return False
        elif comp=='s':
            return True
    elif p1=='s':
        if comp=='p':
            return False
        elif comp=='r':
            return True

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

res=gamewin(You, comp)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

if res==None:
    print("Game Tie")
    engine.say("Game Tie!")
    engine.runAndWait()

elif res:
    print("computer win")
    print("you Lose")
    engine.say("Hey, you lose!")
    engine.runAndWait()

else:
    print("you win")
    print("computer lose")
    engine.say("Hey, You win!")
    engine.runAndWait()

