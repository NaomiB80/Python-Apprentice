"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

# Create a window object
window = Tk()     

# Hide the window, hint: use the withdraw method
window.withdraw()

def add_two_numbers(a, b):
    a = "Type_in_your_first_number"
    b = "Type_in_your_second_number"

    sum_of_two_number = (a + b)
    return "sum_pf_two_numbers"
# Ask the user for the first number   

add =  simpledialog.askinteger("First Number", "Type_in_your_first_number")

# Ask the user for the second number
add =  simpledialog.askinteger("Second Number", "Type_in_your_second_number")

# Display the sum of the two numbers 
messagebox.showinfo('Sum of the two numbers', add_two_numbers)

# Keep the window open
window.mainloop() 
