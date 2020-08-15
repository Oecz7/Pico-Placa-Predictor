from tkinter import *
from tkinter import ttk
import gettext

class Interface:
    def __init__(self):
        
        self.main_window = Tk()
        
        ## Main window title
        self.main_window.title("Pico&Placa Predictor")
        ## Main window size
        self.main_window.geometry("740x360")
        self.main_window.resizable(0,0) 
        ## String variable definition
        self.number = StringVar()
        self.msg = StringVar()
        ## label - text box creation for license plate number
        self.label1 = Label(self.main_window, text = 'License Plate Number', fg='dark slate gray', font= ("Ubuntu Condensed", 10, "bold") )      
        self.txtBox = Entry(self.main_window, textvariable = self.number)
        ## combobox for day selection 
        self.label2 = Label(self.main_window, text = 'Day of the Week', fg='dark slate gray',  font= ("Ubuntu Condensed", 10, "bold"))      
        self.cmb1 = ttk.Combobox(self.main_window)
        self.cmb1["values"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.cmb1.current(0)
        self.cmb1.bind("<<ComboboxSelected>>")
        ## combobox for time selection
        self.label3 = Label(self.main_window, text = 'Hours', fg='dark slate gray',  font= ("Ubuntu Condensed", 10, "bold"))   
        self.picker1 = Spinbox(self.main_window, from_=0, to=24)
        self.label4 = Label(self.main_window, text = 'Minutes', fg='dark slate gray',  font= ("Ubuntu Condensed", 10, "bold"))   
        self.picker2 = Spinbox(self.main_window, from_=0, to=59)
        ## button to request prediction
        self.button1 = Button(self.main_window, text = "Request", command = self.validation)
        ## msg label of the final request
        self.label5 = Label(self.main_window, textvariable= self.msg )
        ## image reference
        self.image = PhotoImage(file="img\placa.png")
        
        self.label6 = Label(self.main_window, image=self.image, bd=0)
        ## Widget's location in the main window
        self.label1.place(x=30, y=40)
        self.txtBox.place(x=225, y=42)
        self.label2.place(x=30, y=80)
        self.cmb1.place(x=225, y=82)
        self.label3.place(x=30, y=120)
        self.picker1.place(x=225, y=122)
        self.label4.place(x=30, y=150)
        self.picker2.place(x=225, y=152)
        self.button1.place(x=30, y=200)
        self.label5.place(x=65, y=250)
        self.label6.place(x=400, y=30)

        self.main_window.mainloop()
        
    ## Validation for days, hours and license plate number
    def validation(self):
        if len(self.number.get()) <= 0:
            self.label5.configure(foreground='steel blue', font=("Ubuntu Condensed", 14) )
            self.msg.set("Please insert a license plate number")
        else :
            flag = 0
            last = len(self.number.get())
            char = self.number.get()[last - 1]
            
            if char.isdecimal():
                
                ## validation for the last digit of the license plate number
                if char == '1'  or char == '2' :

                    if self.cmb1.get() != 'Monday':
                        self.label5.configure(foreground='green')
                        self.msg.set("Could road")
                    
                    elif self.cmb1.get() == 'Monday':
                        flag +=1
                        if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                            flag -=1
                        else:
                            flag +=1
                            
                        if flag == 2:        
                            self.label5.configure(foreground='green')
                            self.msg.set("Could road")
                        
                        else:
                            self.label5.configure(foreground='red')
                            self.msg.set("Could not road")
    
                elif char == '3'  or char == '4':
                    if self.cmb1.get() != 'Tuesday':
                        self.label5.configure(foreground='green')
                        self.msg.set("Could road")
                    
                    elif self.cmb1.get() == 'Tuesday':
                        flag +=1
                        if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                            flag -=1
                        else:
                            flag +=1
                            
                        if flag == 2:        
                            self.label5.configure(foreground='green')
                            self.msg.set("Could road")
                        
                        else:
                            self.label5.configure(foreground='red')
                            self.msg.set("Could not road")

                elif char == '5'  or char == '6':
                    if self.cmb1.get() != 'Wednesday':
                        self.label5.configure(foreground='green')
                        self.msg.set("Could road")
                    
                    elif self.cmb1.get() == 'Wednesday':
                        flag +=1
                        if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                            flag -=1
                        else:
                            flag +=1
                            
                        if flag == 2:        
                            self.label5.configure(foreground='green')
                            self.msg.set("Could road")
                        
                        else:
                            self.label5.configure(foreground='red')
                            self.msg.set("Could not road")

                elif char == '7'  or char == '8':
                    if self.cmb1.get() != 'Thursday':
                        self.label5.configure(foreground='green')
                        self.msg.set("Could road")
                    
                    elif self.cmb1.get() == 'Thursday':
                        flag +=1
                        if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                            flag -=1
                        else:
                            flag +=1
                            
                        if flag == 2:        
                            self.label5.configure(foreground='green')
                            self.msg.set("Could road")
                        
                        else:
                            self.label5.configure(foreground='red')
                            self.msg.set("Could not road")
                    
                elif char == '9' or char == '0':
                    if self.cmb1.get() != 'Friday':
                        self.label5.configure(foreground='green')
                        self.msg.set("Could road")
                    
                    elif self.cmb1.get() == 'Friday':
                        flag +=1
                        if self.picker1.get() >= '7' and self.picker1.get() <= '9' and self.picker2.get() >= '0'  and self.picker2.get() <= '30' or self.picker1.get() >= '16' and self.picker1.get() <= '19' and self.picker2.get() >= '0'  and self.picker2.get() <= '30':
                            flag -=1
                        else:
                            flag +=1
                            
                        if flag == 2:        
                            self.label5.configure(foreground='green')
                            self.msg.set("Could road")
                        
                        else:
                            self.label5.configure(foreground='red')
                            self.msg.set("Could not road")

            else:
                self.label5.configure(foreground='steel blue', font=("Ubuntu Condensed", 14))
                self.msg.set("It is not a valid license plate number \n It must be: PB0-1234")

        

def main():
    app = Interface()
    return 0

if __name__ == '__main__':
    main()

