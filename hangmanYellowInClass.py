# This is my awesome (non-violent) hang person game

from turtle import *
from random import randint
import time

#you dont need this but I do
import math

wordList = ['aberration','abnegation', 'abrogate', \
            'adumbrate', 'anachronistic', 'approbation',\
            'aspersion', 'blandishment', 'defenistrate', \
            'enucleation', 'xylophoage', 'pusillanimous', \
              'fatuous', 'legerdemain', 'maelstrom', 'maudlin', \
            'mendacious', 'partisan', 'predilection', 'trenchant',\
             "St. Mark's School", "New England Patriots", \
            "Let's Snag This Sourdough", "Bag This Baguette" ]


#print(len(wordList))

sw = 800
sh = 850
#sw = 200
#sh = 300
sSide = sw
if sh < sw:
    sSide = sh

s=getscreen()
s.setup(sw, sh)
s.bgcolor('#20f9f9')
t1=getturtle()
t1.speed(0)
t1.hideturtle()
lineW = int(sSide*0.01)
if lineW < 2:
    lineW = 2
t1.width(lineW)
hLeg = int(math.hypot((sw/2), (sh*0.5)))
lAngle = int(math.degrees(math.asin( (sw/2)/hLeg))) #leg angle from bot centerline in deg.
#print("lAngle is {}".format(lAngle))
hArm = int(math.hypot((sw/2), (sh*0.4) )) 
aAngle = int(math.degrees(math.acos( (sw/2)/hArm))) #leg angle from bot centerline in deg.
#print("aAngle is {}".format(aAngle))
RIGHT = True
LEFT = False
nooseX = 0
nooseY = 0
headR = 0

#We need to make 2 turtles
tWriter = Turtle()
tWriter.hideturtle()

tBadLetters = Turtle()
tBadLetters.hideturtle()

#things we need to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord = ""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 6
fontS = int(sh*0.07)
gameDone = False



def displayText(newText):
    tWriter.clear()
    tWriter.color("red")
    tWriter.penup()
    tWriter.goto( -int(sw*0.4), -int(sh*0.4) )
    tWriter.write( newText, font=('Arial', fontS, 'bold') )

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.color("Blue")
    tBadLetters.penup()
    tBadLetters.goto( -int(sw*0.4), int(sh*0.35) )
    tBadLetters.write( newText, font=('Arial', fontS, 'bold') )


def chooseWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is: " + secretWord)

#This def sets up a word display like "__ __ __" for "Cat"
def makeDisplay():
    global displayWord, secretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    #guess = input(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawLeg(RIGHT)
    if fails == 2:
        drawLeg(LEFT)
    if fails == 1:
        drawArm(RIGHT)
    if fails == 0:
        drawArm(LEFT)

def checkWordGuess():
    global gameDone, fails
    boxTitle ="Guess the Word!!!"
    guess = s.textinput(boxTitle, "Enter your guess for the word..")
    if guess.lower() == secretWord.lower():
        displayText("YES!!! " + secretWord + "!!!")
        gameDone = True
    else:
        displayText("No!!! " + guess + " is not word!!!")
        time.sleep(1)
        displayText(displayWord)
        fails -=1
        updateHangmanPerson()

#This def will hold the main running loop for the game        
def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        if theGuess == "$$":
            checkWordGuess()
        # more to come here....
        elif len(theGuess) > 1 or theGuess == "":
            displayText("No!!! " + theGuess + " only one letter, please!")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("No!!! " + theGuess + " not a letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            #letter is correct
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess.lower() not in lettersWrong.lower():
            #letter is wrong
            displayText("No!!! " + theGuess + " is not in word!!!")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Not in word: {" + lettersWrong + "}")
            displayText(displayWord)
            fails -=1
            updateHangmanPerson()
        else:
            # new will give error
            displayText("No!!! " + theGuess + " is already guessed")
            time.sleep(1)
            displayText(displayWord)
        #final conditions to endGame
        if fails <= 0:  # if you run out of guesses
            displayBadLetters("No more guesses")
            displayText("You Lose. Word is : " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("You got it!")
            gameDone = True

        

def drawGallows():
    global nooseX, nooseY

    t1.color('black')
    # draw base
    t1.penup()
    t1.setheading(0)
    t1.goto(-int(sw/6), -int(sh*0.3) )
    t1.pendown()
    t1.forward(int(sw*0.3))
    # draw main pole
    t1.penup()
    t1.backward(int(sw*0.10))
    t1.pendown()
    t1.left(90)
    t1.forward(int(sh*0.60))
    #draw top
    t1.left(90)
    t1.forward(int(sw*0.25))
    #draw hanger
    t1.left(90)
    t1.forward(int(sh*0.10))
    nooseX = t1.xcor()
    nooseY = t1.ycor()
    

def drawHead():
    global headR
    headR = int(sSide*0.08)
    t1.penup()
    t1.goto(t1.xcor()-headR, t1.ycor()-headR)
    t1.pendown()
    t1.circle(headR)
    t1.penup()
    t1.goto(t1.xcor()+headR, t1.ycor()-headR)
    t1.setheading(-90)
    
    
def drawTorso():
    t1.pendown()
    t1.forward(int(sh*0.15))

def drawLeg(whichL):
    #save turtle position
    tx = t1.xcor()
    ty = t1.ycor()
    t1.setheading(-90)
    if(whichL == RIGHT):
        t1.left(lAngle)
    else:
        t1.right(lAngle)
    t1.pendown()
    t1.forward(int(sh*0.15))
    t1.penup()
    t1.goto(tx, ty)
    t1.setheading(-90)
    # good to go

def drawArm(whichA):
    #assumes that turtle is at -90 position
    #assumes that turtle is at bottom of torso
    tx = t1.xcor()  # remember x and y coords for later
    ty = t1.ycor()
    t1.backward(int(sh*0.1))
    if(whichA == RIGHT):
        t1.left(aAngle + 90)
    else:
        t1.right(aAngle + 90)
    t1.pendown()
    t1.forward(int(sw*0.1))
    t1.penup()
    t1.goto(tx, ty)
    t1.setheading(-90)

def drawFace():
    print('hi')
    
    eR = int(sw*0.005)
    #print("eR is {}".format(eR))
    #print("hearR is {}".format(headR))

    for i in range(2):
        t1.penup()
        #drawEyes
        t1.goto(nooseX, nooseY)
        if i % 2 >= 1:
            t1.goto(t1.xcor()-int(headR*0.4 + eR*0.5), t1.ycor()-int(headR*0.6))
        else:
            t1.goto(t1.xcor()+int(headR*0.4 + eR*0.5), t1.ycor()-int(headR*0.6))
        t1.pendown()
        t1.circle(eR)
        t1.penup()
        t1.goto(nooseX, nooseY)

    #drawMouth
    t1.goto(nooseX - int(headR*0.4 + eR*0.8), nooseY-int(headR*1.2))
    t1.pendown()
    mPiece = int( (headR*math.pi)/(10*2) )
    for i in range(3):
        forward(mPiece)
        left(14)
        #t1.showturtle()
    left(10)
    for i in range(7):
        forward(int(mPiece *1.03))
        left(16)
    for i in range(2):
        forward(mPiece)
        left(14)
    
    
            
    
    

#game starts here -- This is the intro
drawGallows()
drawHead()
drawTorso()
drawLeg(RIGHT)
drawLeg(LEFT)
drawArm(RIGHT)
drawArm(LEFT)
drawFace()

#start playing game
time.sleep(1)
t1.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
playGame()






