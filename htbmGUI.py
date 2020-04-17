from tkinter import *
import tkinter as tk
from tkinter import messagebox
import math
import os
import requests


class Window:
    
    def __init__(self, master):
        self.leg1 = .238;
        self.side1 = .859;
        self.angleLeft = 45;
        self.innerRadius = .125
        self.outerRadius = .150
        self.master = master;
        self.valueList = [0,0,0,0,0,0,0]
        #size of user interface
        root.geometry("1000x1000")
        root.title("Automated Hypodermic Tube Bender")
        #creating the buttons, the command atribute calls the function
        self.start()
        #displaying the buttons in the GUI, change relx and rely to move buttons around
        #self.start_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        #self.stop_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    #this function will handle the starting process of the device
    def start(self):
        root.title("Automated Hypodermic Tube Bender")
        self.Restore()
        self.displayCurrentShape()
        self.displayConfig()
        self.displayCurrentShape()

    def displayConfig(self):
        tk.Label(self.w, text="Leg Length:").place(relx=0.1, rely=0.8, anchor=CENTER)
        tk.Label(self.w, text="Side Length:").place(relx=0.4, rely=0.8, anchor=CENTER)
        tk.Label(self.w, text="Inner Radius:").place(relx=0.7, rely=0.8, anchor=CENTER)
        tk.Label(self.w, text="Outer Radius:").place(relx=0.25, rely=0.85, anchor=CENTER)
        tk.Label(self.w, text="Angle Deg:").place(relx=0.55, rely=0.85, anchor=CENTER)
        self.l1 = StringVar()
        self.l1.set(str(self.leg1))
        self.s1 = StringVar()
        self.s1.set(str(self.side1))
        self.aL = StringVar()
        self.aL.set(str(self.angleLeft))
        self.iR = StringVar()
        self.iR.set(str(self.innerRadius))
        self.oR = StringVar()
        self.oR.set(str(self.outerRadius))
        self.valueList[0] = str(float(self.leg1) * 25.4)
        self.valueList[1] = str(self.angleLeft)
        self.valueList[2] = str(float(self.side1) * 25.4)
        self.valueList[3] = str(-(180 - float(self.angleLeft)))
        self.valueList[5] = str(-float(self.angleLeft))
        self.valueList[6] = str((180 - float(self.angleLeft)))


        e1 = tk.Entry(self.w, textvariable=self.l1, justify=RIGHT, width=7) 
        e2 = tk.Entry(self.w, textvariable=self.s1, justify=RIGHT, width=7)
        e3 = tk.Entry(self.w, textvariable=self.iR, justify=RIGHT, width=7)
        e4 = tk.Entry(self.w, textvariable=self.oR, justify=RIGHT, width=7)
        e5 = tk.Entry(self.w, textvariable=self.aL, justify=RIGHT, width=7)

        e1.place(relx=0.19, rely=0.8, anchor=CENTER)
        e2.place(relx=0.49, rely=0.8, anchor=CENTER)
        e3.place(relx=0.79, rely=0.8, anchor=CENTER)
        e4.place(relx=0.34, rely=0.85, anchor=CENTER)
        e5.place(relx=0.64, rely=0.85, anchor=CENTER)
        self.redraw_button = Button(self.w, text="Generate Script", height=2, width=12, bd=3, command=self.generate)
        self.redraw_button.place(relx=0.67, rely=0.9, anchor=CENTER)
        self.redraw_button2 = Button(self.w, text="Draw Tube", height=2, width=12, bd=3, command=self.redraw)
        self.redraw_button2.place(relx=0.27, rely=0.9, anchor=CENTER)


    def generate(self):
        #print(self.serial_ports())
        path = "arduino_script"
        try:  
            os.mkdir(path)
            script = open(path+"/arduino_script.ino", 'w+')
            r = requests.get('https://raw.githubusercontent.com/jls232523/hypodermic_tube_bender/master/arduino_script.ino')
            print(r.text,file=script)
        except OSError as error:  
            script = open(path+"/arduino_script.ino", 'w+') 
            r = requests.get('https://raw.githubusercontent.com/jls232523/hypodermic_tube_bender/master/arduino_script.ino')
            print(r.text,file=script)
        script.close()
        script = open(path+"/arduino_script.ino", 'r')
        script.seek(0,0)
        filedata = script.read()
        script.close()
        newdata = filedata.replace('~',self.valueList[0],1)
        for i in range(1,7):
            newdata = newdata.replace('~',self.valueList[i],1)
        script = open(path+"/arduino_script.ino", 'w')
        script.write(newdata);
        script.close()

    def redraw(self):
        self.leg1 = self.l1.get()
        self.side1 = self.s1.get()
        self.angleLeft = self.aL.get()
        self.innerRadius = self.iR.get()
        self.outerRadius = self.oR.get()

        self.Restore()
        self.displayCurrentShape()
        self.displayConfig()
        self.displayCurrentShape()
        
    def displayCurrentShape(self):
        w = Canvas(self.master, width=1000, height=1000)
        self.w = w
        w.pack()
        inchRatio = 300
        center = 500
        leg1 = float(self.leg1) * inchRatio
        leg2 = float(self.leg1) * inchRatio
        #define values
        middlePart = .1 * inchRatio
        radiusR = float(self.innerRadius)
        radiusL = float(self.innerRadius)
        angleDegR = float(self.angleLeft)
        angleDegL = float(self.angleLeft)
        angleRadR = angleDegR * (math.pi/180)
        angleRadL = angleDegL * (math.pi/180)
        leftSide = float(self.side1);
        rightSide = float(self.side1)
        topRadL = float(self.outerRadius)
        topRadR = float(self.outerRadius)
        topDegL = angleDegL
        topDegR = angleDegR
        topAngleRadR = topDegR * (math.pi/180)
        topAngleRadL = topDegL * (math.pi/180)
        topLength = 1.176

        #Legs
        w.create_line(center, center,center, (center-leg1), fill="darkgreen")
        w.create_line(center+middlePart, center,center+middlePart,(center-leg2), fill="darkgreen")
        #Bottom Angles
        xy = center-(2*radiusR*inchRatio),center-leg1+(radiusR*inchRatio),center,center-leg1-(radiusR*inchRatio)
        xy2 = center+middlePart+(2*radiusL*inchRatio),center-leg2+(radiusL*inchRatio),center+middlePart,center-leg2-(radiusL*inchRatio)

        w.create_arc(xy, start=0, extent=angleDegL, style=tk.ARC, outline="red")
        w.create_arc(xy2, start=180-angleDegR, extent=angleDegR, style=tk.ARC, outline="red")


        
        startCurveLeftX = (center-(radiusL*inchRatio))+(radiusL*inchRatio*math.cos(angleRadL))
        endCurveLeftX = startCurveLeftX - (math.sin(angleRadL) * leftSide * inchRatio)
        startCurveLeftY = center-leg1-(radiusL*inchRatio*math.sin(angleRadL))
        endCurveLeftY = startCurveLeftY - (math.cos(angleRadL) * rightSide * inchRatio)

        startCurveRightX = (center+middlePart+(radiusR*inchRatio))-(radiusR*inchRatio*math.cos(angleRadR))
        endCurveRightX = startCurveRightX + (math.sin(angleRadR) * leftSide * inchRatio)
        startCurveRightY = center-leg1-(radiusR*inchRatio*math.sin(angleRadR))
        endCurveRightY = startCurveRightY - (math.cos(angleRadR) * rightSide * inchRatio)

        #Sides
        w.create_line(startCurveLeftX,startCurveLeftY,endCurveLeftX,endCurveLeftY, fill="darkgreen")
        w.create_line(startCurveRightX,startCurveRightY,endCurveRightX,endCurveRightY, fill="darkgreen")
        sx3 = endCurveLeftX-(inchRatio*topRadL)+(inchRatio*topRadL*math.cos(angleRadL))
        sy3 = endCurveLeftY-(topRadL*inchRatio)-(inchRatio*topRadL*math.sin(angleRadL))
        xy3 = sx3,sy3,sx3+2*topRadL*inchRatio,sy3+2*topRadL*inchRatio

        # Top Curves
        sxR3 = endCurveRightX+(inchRatio*topRadR)-(inchRatio*topRadR*math.cos(angleRadR))
        syR3 = endCurveRightY-(topRadR*inchRatio)-(inchRatio*topRadR*math.sin(angleRadR))
        xy4 = sxR3,syR3,sxR3-2*topRadR*inchRatio,syR3+2*topRadR*inchRatio

        w.create_arc(xy3, start=180+angleDegL-(90+topDegL), extent=90+topDegL, style=tk.ARC, outline="red")
        w.create_arc(xy4, start= (-angleDegR), extent=90+topDegR, style=tk.ARC, outline="red")

        #Debug
        #w.create_rectangle(xy)
        #w.create_rectangle(xy2)
        #w.create_rectangle(xy3)
        #w.create_rectangle(xy4)

        #Top
        w.create_line(sx3+(topRadL*inchRatio),syR3 ,sxR3-(inchRatio*topRadR), syR3, fill="darkgreen")
        p1 = [sx3+(topRadL*inchRatio), syR3]
        p2 = [sxR3-(inchRatio*topRadR), syR3]
        distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ) / inchRatio
        self.valueList[4] = str(distance * 25.4)
    def stop(self):
        root.title("Stop Operations")

    #this function remove all the widgets(buttons)
    def Restore(self):
            for widgets in root.winfo_children():
                widgets.destroy()
    #when back button is pressed we delite all widgets and call the contructor to displayed our previos window
    def back(self):
        self.Restore()
        self.__init__(root)


root = Tk()

run = Window(root)

root.mainloop()
