from connections import *

def camtrig_test():
    print("\n ******Beginning Camera Trigger Test******** \n")
    for i in range(20):
        if GPIO.input(GPIO1):
            print "GPIO1.HIGH/True - button pressed"
        else:
            print "GPIO1.LOW/False - button not pressed"
        sleep(.5)
    print("\n **********Ending ADC Test********** \n")


if __name__ == "__main__":
    camtrig_test()
