from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissors Game")
root.configure(background="skyblue")

#images
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rockcomp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("papercomp.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissorscomp.png"))

#insert pictures
user_label = Label(root,image=scissors_img,bg="purple")
comp_label = Label(root,image=scissors_img_comp,bg="purple")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
player_score = Label(root,text=0,font=100,bg="skyblue",fg="white")
computer_score = Label(root,text=0,font=100,bg="skyblue",fg="white")
computer_score.grid(row=1, column=1)
player_score.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER'S SCORE",bg="skyblue").grid(row=0,column=3)
comp_indicator = Label(root,font=50,text="COMPUTER'S SCORE",bg="skyblue").grid(row=0,column=1)

#update choices
choices = ["rock","paper","scissors"]
def updateChoice(x):
#for computer
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp) 
    else:
        comp_label.configure(image=scissors_img_comp)    
        
#user      
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)    
    checkWin(x,compchoice)    
              
#buttons
rock = Button(root, width=20,height=2,text="ROCK",bg="red",fg="white",command=lambda:updateChoice("rock")).grid(row = 2,column=1)
paper = Button(root, width=20,height=2,text="PAPER",bg="green",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors = Button(root, width=20,height=2,text="SCISSORS",bg="blue",fg="white",command=lambda:updateChoice("scissors")).grid(row=2,column=3)

#messages
msg = Label(root, font=50,bg="skyblue", fg="white")
msg.grid(row=3,column=2)

#update messages
def updateMessage(x):
    msg['text'] = x
    
#user score update
def updateScore(Player):
    if Player =="user":
        score = int(player_score["text"])
        score += 1
        player_score["text"] = str(score)
        
#computer score
    elif Player == "computer":
        score = int(computer_score["text"])
        score += 1
        computer_score["text"] = str(score)
        
#check winner messages
def checkWin(Player,computer):
    if Player == computer:
        updateMessage("It is a Tie")
    elif Player == "rock":  
        if computer == "paper":
            updateMessage("You lose!!")
            updateScore("computer")
        else:
            updateMessage("You win!!YAAAY")
            updateScore("user")
    elif Player == "paper":
        if computer == "scissors":
            updateMessage("You lose!!")
            updateScore("computer")
        else:
            updateMessage("You win!!YAAAY")
            updateScore("user")
    elif Player == "scissors":
        if computer == "rock":
            updateMessage("You lose!!")
            updateScore("computer")
        else:
            updateMessage("You win!!YAAAY")
            updateScore("user")
    else:
        pass             
                          
root.mainloop()