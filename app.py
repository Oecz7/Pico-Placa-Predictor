from tkinter import *
from tkinter import ttk
import gettext

class Interface:
    def __init__(self):
        
        self.main_window = Tk()
        
        ## Main window title
        self.main_window.title("Predictor")
        ## Main window size
        self.main_window.geometry("640x360")
        ## String variable definition
        self.number = StringVar()
        self.msg = StringVar()
        ## label - text box creation for license plate number
        self.label1 = Label(self.main_window, text = 'Insert License Plate Number')      
        self.txtBox = Entry(self.main_window, textvariable = self.number)
        ## combobox for day selection 
        self.label2 = Label(self.main_window, text = 'Day of the Week')      
        self.cmb1 = ttk.Combobox(self.main_window)
        self.cmb1["values"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.cmb1.bind("<<ComboboxSelected>>")
        ## combobox for time selection
        self.label3 = Label(self.main_window, text = 'Select Hour')   
        self.picker1 = Spinbox(self.main_window, from_=0, to=24)
        self.label4 = Label(self.main_window, text = 'Select Minute')   
        self.picker2 = Spinbox(self.main_window, from_=0, to=59)
        ## button to request prediction
        self.button1 = Button(self.main_window, text = "Request", command = self.validation)
        ## msg label of the final request
        self.label5 = Label(self.main_window, textvariable= self.msg, foreground = 'red' )
        ## Widget's location in the main window
        self.label1.place(x=30, y=40)
        self.txtBox.place(x=300, y=42)
        self.label2.place(x=30, y=80)
        self.cmb1.place(x=300, y=82)
        self.label3.place(x=30, y=120)
        self.picker1.place(x=300, y=122)
        self.label4.place(x=30, y=150)
        self.picker2.place(x=300, y=152)
        self.button1.place(x=30, y=200)
        self.label5.place(x=30, y=230)

        self.main_window.mainloop()
        
        
    def validation(self):
        flag = 0
        last = len(self.number.get())
        char = self.number.get()[last - 1]

        if char == '1'  or char == '2' :

            if self.cmb1.get() != 'Monday':
                self.label5.configure(foreground='red')
                self.msg.set("Could road")
            
            elif self.cmb1.get() == 'Monday':
                flag +=1
                if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                    flag -=1
                else:
                    flag +=1
                    
                if flag == 2:        
                    self.label5.configure(foreground='red')
                    self.msg.set("Could road")
                
                else:
                    self.label5.configure(foreground='red')
                    self.msg.set("Could not road")

            
            
        
        elif char == '3'  or char == '4':
            if self.cmb1.get() != 'Tuesday':
                self.label5.configure(foreground='red')
                self.msg.set("Could road")
            
            elif self.cmb1.get() == 'Tuesday':
                flag +=1
                if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                    flag -=1
                else:
                    flag +=1
                    
                if flag == 2:        
                    self.label5.configure(foreground='red')
                    self.msg.set("Could road")
                
                else:
                    self.label5.configure(foreground='red')
                    self.msg.set("Could not road")

        elif char == '5'  or char == '6':
            if self.cmb1.get() != 'Wednesday':
                self.label5.configure(foreground='red')
                self.msg.set("Could road")
            
            elif self.cmb1.get() == 'Wednesday':
                flag +=1
                if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                    flag -=1
                else:
                    flag +=1
                    
                if flag == 2:        
                    self.label5.configure(foreground='red')
                    self.msg.set("Could road")
                
                else:
                    self.label5.configure(foreground='red')
                    self.msg.set("Could not road")
        elif char == '7'  or char == '8':
            if self.cmb1.get() != 'Thursday':
                self.label5.configure(foreground='red')
                self.msg.set("Could road")
            
            elif self.cmb1.get() == 'Thursday':
                flag +=1
                if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                    flag -=1
                else:
                    flag +=1
                    
                if flag == 2:        
                    self.label5.configure(foreground='red')
                    self.msg.set("Could road")
                
                else:
                    self.label5.configure(foreground='red')
                    self.msg.set("Could not road")
            
        elif char == '9' or char == '0':
            if self.cmb1.get() != 'Friday':
                self.label5.configure(foreground='red')
                self.msg.set("Could road")
            
            elif self.cmb1.get() == 'Friday':
                flag +=1
                if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                    flag -=1
                else:
                    flag +=1
                    
                if flag == 2:        
                    self.label5.configure(foreground='red')
                    self.msg.set("Could road")
                
                else:
                    self.label5.configure(foreground='red')
                    self.msg.set("Could not road")
           

def main():
    app = Interface()
    return 0

if __name__ == '__main__':
    main()

