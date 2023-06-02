from body import move
from body import sense

class Drive:
    def __init__(self):
        self.mode = "manual"
        self.speed=50

    def set_mode(self,mode):
        if mode=="manual" or mode=="autonomous":
            self.mode = mode
            print("mode set as",self.mode)
        else:
            print("invalid mode")

    def set_speed(self,speed):
        if(speed>0 and speed<100):
            self.speed=speed

    def go(self,msg):
        if self.mode=="manual":
            self.manual(msg)
        if self.mode=="autonomous":
            self.autonomous(msg)

    def manual(self,msg):
        print("im inside manual")
        #check sensors for obstacles here
        if(msg=="left"):
            move.turnLeft(self.speed)
        if(msg=="right"):
            move.turnRight(self.speed)
        if(msg=="stop"):
            move.stopMoving(self.speed)
        if(msg=="go"):
            move.goForward(self.speed)



    def autonomous(self,msg):
        pass