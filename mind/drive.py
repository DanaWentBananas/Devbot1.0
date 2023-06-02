from body import move
from body import sense

class Drive:
    def __init__(self):
        self.mode = "manual"

    def set_mode(self,mode):
        if mode=="manual" or mode=="autonomous":
            self.mode = mode
            print("mode set as",self.mode)
        else:
            print("invalid mode")

    def go(self,msg):
        if self.mode=="manual":
            self.manual(msg)
        if self.mode=="autonomous":
            self.autonomous(msg)

    def manual(self,msg):
        print("im inside manual")
        #check sensors for obstacles here
        if(msg=="left"):
            move.turnLeft()
        if(msg=="right"):
            move.turnRight
        if(msg=="stop"):
            move.stopMoving()
        if(msg=="go"):
            move.goForward()



    def autonomous(self,msg):
        pass