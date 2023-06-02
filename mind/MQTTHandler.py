from mind import drive as d

drive = d.Drive()

def handle(msg):
    print("message being handled..")
    if msg=="forward" or msg=="left" or msg=="right" or msg=="stop":
        drive.go(msg)
