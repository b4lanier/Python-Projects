
# parent class
class School:
    name="unknown"
    size=None
    colors="Blue and White"

    def information(self):  #parent method
        msg="\nName: {}\nSize: {}\nColors: {}".format(self.name,self.size,self.colors)
        return msg

# child class
class History (School):
    name='History Class'
    size=30
    # use colors inhereted from parent

    def exam(self):   #child method
        msg="\nStudy for an exam this Friday"
        return msg

# 2nd child class
class Math (School):
    name='Math Class'
    size=20

    def assignment(self):  #child method
        msg="\nDo all the even problems"
        return msg



if __name__=="__main__":
    history=History() #run one method from parent and one from child
    print(history.information())
    print(history.exam())

    math=Math()  #second child methods
    print(math.information())
    print(math.assignment())
