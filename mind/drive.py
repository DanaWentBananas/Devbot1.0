from body import move

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


    def autonomous(self,msg):
        pass