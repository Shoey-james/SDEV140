"""
James Shoemaker SDEV140 3/4/24
Calculator - Final Project


"""




import tkinter as tk
from tkinter import messagebox
# Create Calculator Class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # Labeling application
        root.geometry("400x550")       # format size of window for calculator
        self.root.configure(bg="black") # set background of window
        
        # Initialize variables
        self.expression = ""
        self.result_var = tk.StringVar()
        
        # Load the images
        self.icon_image = tk.PhotoImage(file="equal.png").subsample(4,4)            # subsample resizes images
        self.clear_image = tk.PhotoImage(file="clear.png").subsample(4,3)           

        # label images and position them
        self.icon_label = tk.Label(root, image=self.icon_image)
        self.icon_label.grid(row=0, column=0, columnspan=4)
        #self.icon_label.place(x=25, y=25)

        # Create a Clear button with image
        self.clear_button = tk.Button(root, image=self.clear_image, bd=0, command=self.clearbutton)
        self.clear_button.grid(row=1, column=3)
        # Create an Equal button with image
        self.equal_button = tk.Button(root, image=self.icon_image, bd=0, command=self.equalbutton)
        self.equal_button.grid(row=2, column=3)
        # User Entry Area 
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 20), bd=5, relief="ridge", justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15)

        # Define the buttons for the calculator and position them
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),                      # removed "C" button to use an image as the clear button
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), 
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), 
            ('.', 4, 0), ('0', 4, 1), ('+', 4, 2),
            ('/', 5, 0), ('*', 5, 1), ('-', 5, 2),
            ('(', 3, 3), (')', 4, 3)                  
        ]
        
        # Create buttons and attach commands to them
        for (text, row, col) in buttons:
            b = tk.Button(root, text=text, font=('Arial', 20), width=3, height=1, bd=5, relief="ridge",
                          command=lambda t=text: self.on_button_click(t), fg="black",bg="purple")           # added some colors to buttons and font
            b.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    
    # defining functions to occur on button click
    def on_button_click(self, value):
        if value == '=':
            result = eval(self.expression)
            self.result_var.set(result)
        #elif value == 'C':                                         # commented out to allow image to act as "C" button instead
            #self.expression = ""
            #self.result_var.set("")
        else:
            self.expression += value
            self.result_var.set(self.expression)
            if "/0" in self.expression:                             # division by zero validation
                messagebox.showerror("Division by zero error")
    # define function for clicking clear button image        
    def clearbutton(self):
        self.expression = ""
        self.result_var.set("")
    # define function for clicking equal button image    
    def equalbutton(self):
        result = eval(self.expression)
        self.result_var.set(result)
# defining main
def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
# execute main
if __name__ == "__main__":
    main()
