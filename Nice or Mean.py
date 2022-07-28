
def start(nice=0,mean=0,name=""):  #assign default values to parameters. won't override passed-in values
    name=describe_game(name) # get user's name
    nice,mean,name-nice_mean(nice,mean,name) #set 3 variables from that function

def describe_game(name):
    #check if new game, if new-get name, if not-thank and continue
    if name !="":  #empty name is passed from start()
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop=True
        while stop:
            if name=="":  #if empty, get name and capitalize
                name=input("\nWhat is your name? \n>>> ").capitalize() 
                if name !="": #describe game and break while loop
                    print("\nWelcome, {}!".format(name))
                    print("\$Recycle.Bin")
                    print("but at the endof the game, your fate will be sealed by your actions.")
                    stop=False
    return name

def nice_mean(nice,mean,name): #start with nice=0,mean=0,name
    stop=True
    while stop: #loop until they give valid input, which we store lowercase
        show_score(nice,mean,name) #pass 3 variables to show_score()
        pick=input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick=="n":
            print("\nThe stranger walks away smiling...")
            nice=nice+1
            stop=False #break loop after adding to score
        if pick=="m":
            print("\nThe stranger glares and storms off...")
            mean=mean+1
            stop=False
    score(nice,mean,name) #pass 3 variables to score()

def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({} Mean)".format(name, nice, mean))

def score(nice,mean,name):    #score function is passed the values stored in 3 variables
    if nice>2:  #call 1 of 3 methods, based on scores
        win(nice,mean,name)
    if mean>2:
        lose(nice,mean,name)
    else:  #go back and ask the question if there is no winning or losing score
        nice_mean(nice,mean,name)

def win(nice, mean,name):
    print("\nNice job {}, you win! \nEveryone loves you!".format(name))
    again(nice,mean,name) #ask if want to play again

def lose(nice, mean,name):
    print("\nToo bad, game over, {}! \nyou live alone in a van by the river!".format(name))
    again(nice,mean,name) #ask if want to play again

def again(nice,mean,name):
    stop=True
    while stop:
        choice=input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice=="y": #stop loop and call reset()
            stop=False
            reset(nice,mean,name)
        if choice=="n":#stop loop and call quit()
            print("\nSorry to see you go!")
            stop=False
            quit() #built-in python function
        else: #message and continue loop if no valid input
            print("\nEnter ( Y ) for 'Yes' or ( N ) for 'No':\n>>> ")

def reset(nice,mean,name):
    nice=0 #reset scores, keep name value
    mean=0
    start(nice,mean,name)



if __name__=="__main__":
    start()
