from tkinter import *

from random import*

 

def add_problem():

    global x

    global y

    global problem_label

    global answer_entry

    global problem_text

    x = randrange(100)

    y = randrange(100)

   

    problem_text = str(x) + " + " + str(y) + " = "

    problem_label.configure(text = problem_text, bg = "lightblue", font= ("Times", "20", "bold"))

    answer_entry.focus()

 

def sub_problem():

    global x

    global y

    global problem_label

    global answer_entry

    global problem_text

    x = randrange(100)

    y = randrange(100)

   

    problem_text = str(x) + " - " + str(y) + " = "

    problem_label.configure(text = problem_text, bg = "lightblue", font= ("Times", "20", "bold"))

    answer_entry.focus()

 

def mult_problem():

    global x

    global y

    global problem_label

    global answer_entry

    global problem_text

    x = randrange(15)

    y = randrange(15)

   

    problem_text = str(x) + " x " + str(y) + " = "

    problem_label.configure(text = problem_text, bg = "lightblue", font= ("Times", "20", "bold"))

    answer_entry.focus()

   

def add_check_answer():

    global answer_entry

   

    answer = x + y

   

    try:

        user_answer = int(answer_entry.get())

        if user_answer == answer:

            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")

            answer_entry.delete(0, END)

            add_problem()

        else:

            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue")

            answer_entry.delete(0, END)

            add_problem()

    except ValueError:

        feedback.configure(text = "That is not a number", bg = "lightblue")

        answer_entry.delete(0, END)

        answer_entry.focus()

 

def sub_check_answer():

    global answer_entry

   

    answer = x - y

   

    try:

        user_answer = int(answer_entry.get())

        if user_answer == answer:

            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")

            answer_entry.delete(0, END)

            sub_problem()

        else:

            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue")

            answer_entry.delete(0, END)

            sub_problem()

    except ValueError:

        feedback.configure(text = "That is not a number", bg = "lightblue")

        answer_entry.delete(0, END)

        answer_entry.focus()

 

def mult_check_answer():

    global answer_entry

   

    answer = x * y

   

    try:

        user_answer = int(answer_entry.get())

        if user_answer == answer:

            feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")

            answer_entry.delete(0, END)

            mult_problem()

        else:

            feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue")

            answer_entry.delete(0, END)

            mult_problem()

    except ValueError:

        feedback.configure(text = "That is not a number", bg = "lightblue")

        answer_entry.delete(0, END)

        answer_entry.focus()

 

def Home ():

    global frame1

    global frame2

   

    frame2.grid_remove()

    frame1 = LabelFrame(root, bg = "lime green", height = 300)

    frame1.grid(row=0, column = 0)

   

    TitleLabel = Label (frame1, bg = "lime green", fg = "white", width = 20, padx = 30, pady = 10, text = "Welcome to Maths Quiz V3", font= ("Times", "25", "bold"))

    TitleLabel.grid(columnspan = 5)

   

    button1 = Button(frame1, text = "Addition", font =("bold", "15"), bg = "white", anchor = W, command = Addition)

    button1.grid(row = 8, column = 2)

 

    button2 = Button(frame1, text = "Subtraction", font =("bold", "15"), bg = "white", anchor = W, command = Subtraction)

    button2.grid(row = 9, column = 2)

 

    button3 = Button(frame1, text = "Multiplication", font =("bold", "15"), bg = "white", anchor = W, command = Multiply)

    button3.grid(row = 10, column = 2)

   

def Addition():  

    global frame1

    global frame2     

    global problem_label

    global answer_entry

    global feedback

    global x

    global y

   

    frame1.grid_remove()

    frame2 = LabelFrame(root, height = "600", width = "300", bg = "lightblue")

    frame2.grid(row=0, column = 0)

   

    problem_label = Label(frame2, text = "", width = 18, height = 3)

    problem_label.grid(row = 0, column = 0, sticky = W)

   

    answer_entry = Entry(frame2, width = 7)

    answer_entry.grid(row = 0, column = 1, sticky = W)

   

    check_btn = Button(frame2, text = "Check Answer", bg = "white", font= ("Times", "15"), command = add_check_answer, relief = RIDGE)

    check_btn.grid(row = 1, column = 1)

   

    feedback = Label(frame2, text = "", font= ("Times", "15"), height = 3, bg = "lightblue")

    feedback.grid(row = 2, column = 0)

 

    home = Button(frame2, text = "Home", font= ("Times", "15"), anchor = W, command = Home)

    home.grid(row = 1, column = 0)

 

    add_problem()

 

def Subtraction():

    global frame1

    global frame2   

    global problem_label

    global answer_entry

    global feedback

    global x

    global y

 

    frame1.grid_remove()

    frame2 = LabelFrame(root, height = "600", width = "300", bg = "lightblue")

    frame2.grid(row=0, column = 0)

   

    problem_label = Label(frame2, text = "", width = 18, height = 3)

    problem_label.grid(row = 0, column = 0, sticky = W)

   

    answer_entry = Entry(frame2, width = 7)

    answer_entry.grid(row = 0, column = 1, sticky = W)

   

    check_btn = Button(frame2, text = "Check Answer", bg = "white", font= ("Times", "15"), command = sub_check_answer, relief = RIDGE)

    check_btn.grid(row = 1, column = 1)

   

    feedback = Label(frame2, text = "", font= ("Times", "15"), height = 3, bg = "lightblue")

    feedback.grid(row = 2, column = 0)

 

    home = Button(frame2, text = "Home", font= ("Times", "15"), anchor = W, command = Home)

    home.grid(row = 1, column = 0)

 

    sub_problem()

 

def Multiply():

    global frame1

    global frame2   

    global problem_label

    global answer_entry

    global feedback

    global x

    global y

 

    frame1.grid_remove()

    frame2 = LabelFrame(root, height = "600", width = "300", bg = "lightblue")

    frame2.grid(row=0, column = 0)

   

    problem_label = Label(frame2, text = "", width = 18, height = 3)

    problem_label.grid(row = 0, column = 0, sticky = W)

   

    answer_entry = Entry(frame2, width = 7)

    answer_entry.grid(row = 0, column = 1, sticky = W)

   

    check_btn = Button(frame2, text = "Check Answer", bg = "white", font= ("Times", "15"), command = mult_check_answer, relief = RIDGE)

    check_btn.grid(row = 1, column = 1)

   

    feedback = Label(frame2, text = "", font= ("Times", "15"), height = 3, bg = "lightblue")

    feedback.grid(row = 2, column = 0)

 

    home = Button(frame2, text = "Home", font= ("Times", "15"), anchor = W, command = Home)

    home.grid(row = 1, column = 0)

 

    mult_problem()

 

   

    

root = Tk()

root.title("Maths Quiz V3")

root.geometry("600x300+700+10")

frame1 = Frame(root)

frame2 = Frame(root)

 

Home()

 

root.mainloop()
