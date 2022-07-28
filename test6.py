def getInfo():
    var1=input("\nPlease provide first numeric value: ")
    var2=input("\nPlease provide second numeric value: ")
    return(var1,var2) #pass the variables input above

def compute():
    go=True
    while go:
        var1,var2=getInfo()
        try:  #error handling if bad input. If good, do the math below
            var3=int(var1) +int(var2)
            go=False  #if input is valid, exit the while loop
        except ValueError as e: #if value error, store error as e and print below
            print("{}: \n\nYou did not provide a numeric value.".format(e))
        except: #different type of error, not value
            print("\n\nOops, you provided invalid input.")
        finally: #catches all other kinds of errors
            print("moving on...")
    print("{} + {} = {}".format(var1,var2,var3))

if __name__ == "__main__": #run getInfo if this is the main, not a called app
    compute()
