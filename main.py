from tkinter import *
import tkinter.messagebox
# tk window + title
window = Tk()
# Add image file
back_im = PhotoImage(file="BG2.png")
lg_bg = PhotoImage(file="LG_BG.PNG")
sg_bg= PhotoImage(file="SG_BG.PNG")
cn_bg= PhotoImage(file="CN_BG.PNG")
logo = PhotoImage(file="Logo.png")
Sign_in = PhotoImage(file="Sign_in.png")
Sign_up = PhotoImage(file="Sign_up.png")
tk_bg = PhotoImage(file="Ticket.PNG")
map = PhotoImage(file="Map.png")
next = PhotoImage(file="Arrow.png")
wt_bg= PhotoImage(file="BG.png")
wheel=PhotoImage(file="Wheel.png")
bg_6= PhotoImage(file="bg_6.png")
bk= PhotoImage(file="bKash.png")
ng= PhotoImage(file="Nagad.png")
rc= PhotoImage(file="Rocket.png")
cn_bt= PhotoImage(file="Cancel_bt.png")
#ceat counter
c=0
#distance counter
d=0
#booked seats
bs=[]
#Total Fair
tf=0
#bus no
bus_no=''
sd=''
fd=''
time=''


def front():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    def s_in():
        window.quit()
        sign_in()

    def s_up():
        window.quit()
        sign_up()

    # BG Image
    Label(window, image=back_im, border=0).place(x=0, y=0)

    # Button
    Button(window, image=Sign_in, bg='#CF7BFF',fg='#CF7BFF', border="0", command=lambda: s_in(),  relief=GROOVE
           ).place(x=50, y=450)

    Button(window, image=Sign_up,bg='#CF7BFF',fg='#CF7BFF', border="0", command=lambda: s_up(),  relief=GROOVE
           ).place(x=50, y=510)

    # running main loop
    window.mainloop()

def sign_in():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    def s_in():
        window.quit()
        page_4()

    def s_up():
        window.quit()
        sign_up()

    # BG Image
    Label(window, image=lg_bg, border=0).place(x=0, y=0)

    # Button and lebels

    Entry(window, width=26, bg="white", font='roboto 12 bold').place(x=63, y=380)
    Entry(window, width=26, bg="white", font='roboto 12 bold', show='*').place(x=63, y=445)
    Button(window, text='Login', command=lambda: s_in(), font='roboto 9 bold', bg='#fbdb47', relief=RIDGE).place(
        x=280, y=525)
    Label(window, text='Don\'t have an account?. Click', font='roboto 10 bold', fg='Black', bg='#CF73FF').place(x=60, y=590)
    Button(window, text='SIGN UP', command=lambda: s_up(), font='roboto 8 bold', bg='#fbdb47', relief=RIDGE).place(
        x=270, y=590)

    # running main loop
    window.mainloop()


def sign_up():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    def s_in():
        window.quit()
        sign_in()

    def s_up():
        window.quit()
        page_4()

    # BG Image
    Label(window, image=sg_bg, border=0).place(x=0, y=0)

    # Button
    # createing text box
    Entry(window, width=26, bg="white", font='roboto 12 bold').place(x=63, y=164)
    Entry(window, width=26, bg="white", font='roboto 12 bold').place(x=63, y=217)
    Entry(window, width=26, bg="white", font='roboto 12 bold').place(x=63, y=270)
    Entry(window, width=26, bg="white", font='roboto 12 bold',show='*').place(x=63, y=319)
    Entry(window, width=34, bg="white", font='roboto 10 bold',show='*').place(x=63, y=366)


    Button(window, text='Sign Up', command=lambda: s_up(), font='roboto 9 bold', bg='#fbdb47', relief=RIDGE).place(
        x=277, y=425)
    Label(window, text='Already have an account. Click', font='roboto 10 bold', fg='Black', bg='#CF7BFF').place(x=80, y=560)
    Button(window, text='SIGN IN', command=lambda: s_in(), font='roboto 9 bold', bg='#fbdb47', relief=RIDGE).place(
        x=250, y=560)

    # running main loop
    window.mainloop()



def page_4():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")
    global c
    c = 0
    global bs
    bs.clear()
    location = ["Dhanmondi", "Mohammadpur", "Shyamoli", "Kallyanpur", "New Market"]

    # BG Image
    Label(window, image=map, border=0).place(x=0, y=0)
    #get value from option


    # Frame
    frame = Frame(window, padx=30, pady=30)
    frame.config(background='#AFA6F9')
    frame.place(x=50, y=30)
    # Label(frame, text='Time : ', font='Arial 10 bold', width=8, fg='Black',bg='#CF7BFF').pack(padx=30,pady=30)
    variable1 = StringVar(frame)
    variable1.set(location[0])
    variable2 = StringVar(frame)
    variable2.set(location[0])

    entry=Entry(frame, width=17)
    entry.grid(row=3, column=2)

    loc = OptionMenu(frame,variable1, *location)
    loc.grid(row=1, column=2)
    loc.config(bg='Yellow', border=0)
    des = OptionMenu(frame, variable2, *location)
    des.grid(row=2, column=2)
    des.config(bg='Yellow', border=0)
    Button(frame, image=next, relief=RIDGE, border=0, bg='#AFA6F9', command=lambda: nxt_pg()).grid(row=4, column=4)
    Label(frame, text='Time           :', bg='#AFA6F9',font='roboto 10 bold').grid(row=3, column=1)
    Label(frame, text='Location     :', bg='#AFA6F9',font='roboto 10 bold').grid(row=1, column=1)
    Label(frame, text='Destination :', bg='#AFA6F9',font='roboto 10 bold').grid(row=2, column=1)


    def nxt_pg():
        global sd
        global fd
        global time
        time = entry.get()
        sd=variable1.get()
        fd=variable2.get()
        s=0
        f=0
        for x in range(5):
            if sd==location[x]:
                s=x
            elif fd==location[x]:
                f=x
        global d
        d = abs(f - s)

        Button(window, text='BR-13717', font='roboto 12 bold', relief=RIDGE, bg='#AFA6F9', border=0,
               command=lambda: br_1(),padx=10,pady=10).place(x=70, y=500)
        Button(window, text='BR-13645', font='roboto 12 bold', relief=RIDGE, bg='#AFA6F9', border=0,
               command=lambda: br_2(),padx=10,pady=10).place(x=200, y=500)
    def br_1():
        global bus_no
        bus_no='BR-13717'
        window.quit()
        page_5()

    def br_2():
        global bus_no
        bus_no = 'BR-13645'
        window.quit()
        page_5()

    # running main loop
    window.mainloop()


def page_5():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    def nt_pg():
        window.quit()
        page_6()
    def bc_pg():
        window.quit()
        page_4()
    # BG Image
    Label(window, image=wt_bg, border=0).place(x=0, y=0)
    Label(window, text='Seat Selection', bg='#db9dff', fg='Black',font='roboto 12 bold').place(x=30,y=30)
    # Frame
    frame = Frame(window, padx=10, pady=10)
    frame.config(background='#AFA6F9')
    frame.place(x=80, y=80)
    Label(frame, image=wheel,bg='#AFA6F9', border=0).place(x=110,y=0)

    # Instruction to select seat
    Button(window,relief=RIDGE, bg='blue',width=2, height=1, border=0,state=DISABLED).place(x=55, y=435)
    Label(window,text='Selected', font='roboto 8 bold',bg='#db9dff').place(x=82, y=435)
    Button(window, relief=RIDGE, bg='White', width=2, height=1, border=0, state=DISABLED).place(x=145, y=435)
    Label(window, text='Available', font='roboto 8 bold', bg='#db9dff').place(x=168, y=435)
    Button(window, relief=RIDGE, bg='#6A6C6D', width=2, height=1, border=0, state=DISABLED).place(x=230, y=435)
    Label(window, text='Booked', font='roboto 8 bold', bg='#db9dff').place(x=258, y=435)

    Label(window, text='Booked Seats : ', font='roboto 10 bold', bg='#db9dff').place(x=50, y=475)

    def appear(index):
        # This line would be where you insert the letter in the textbox
        global c
        global d
        c+=1
        Label(window, text=f'{letters[index]}', bg='#db9dff',fg='Black').place(x=130+(20*c),y=476)
        global tf
        tf=d*c*10
        global bs
        bs.append(letters[index])
        Label(window, text=f'Total Fare : {tf}', bg='#db9dff', fg='Black', font='roboto 10 bold').place(x=50, y=520)
        # Disable the button by index
        buttons[index].config(background="blue")
        buttons[index].config(state="disabled")

        # Process and Cancel button

        Button(window, text='Proceed to payment', font='roboto 8 bold', relief=RIDGE, bg='#FFFFFF', border=0,
               command=lambda: nt_pg()).place(x=190, y=600)
        Button(window, text='Cancel Selection', font='roboto 8 bold', relief=RIDGE, bg='#FFFFFF', border=0,
               command=lambda: bc_pg()).place(x=50, y=600)

    letters = ["01", "02", "03", "04", "05", "06", "07", "08", "09","10","11", "12", "13", "14", "15", "16", "17", "18", "19","20","21", "22", "23", "24", "25", "26", "27", "28", "29","30","31", "32", "33", "34", "35", "36", "37", "38", "39","40","41","42"]

    # A collection (list) to hold the references to the buttons created below
    buttons = []
    ro=0
    co=0
    for index in range(0,41):
        n = letters[index]
        if index<4:
            co=index%2
            ro=index//2
            button = Button(frame, bg="white", text=n, width=3, height=1, relief=GROOVE,command=lambda index=index, : appear(index))

            # Add the button to the window
            button.grid(padx=2, pady=2, row=ro, column=co)

            # Add a reference to the button to 'buttons'
            buttons.append(button)
        elif (index>=36):
            co = index % 4
            ro = (index // 4)+1
            if index==40:
                ro-=1
                co=4
            button = Button(frame, bg="white", text=n, width=3, height=1, relief=GROOVE,
                            command=lambda index=index,: appear(index))

            # Add the button to the window
            button.grid(padx=2, pady=2, row=ro, column=co)

            # Add a reference to the button to 'buttons'
            buttons.append(button)
        else:
            co = index % 4
            ro = (index // 4)+1
            button = Button(frame, bg="white", text=n, width=3, height=1, relief=GROOVE,
                            command=lambda index=index : appear(index))

            # Add the button to the window
            if (index<36) and ((index%4)>1):
                button.grid(padx=2, pady=2, row=ro, column=co+1)
            else:
                button.grid(padx=2, pady=2, row=ro, column=co)

            # Add a reference to the button to 'buttons'
            buttons.append(button)


    # running main loop
    window.mainloop()

def page_6():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    global bs

    global tf

    # BG Image
    Label(window, image=bg_6, border=0).place(x=0, y=0)
    Button(window, image=bk, relief=GROOVE,bg='white',height=65,command=lambda: con()).place(x=58,y=163)
    Button(window, image=rc, relief=GROOVE,bg='white',height=65,command=lambda: con()).place(x=150,y=163)
    Button(window, image=ng, relief=GROOVE,bg='white',height=65,command=lambda: con()).place(x=240,y=163)
    Label(window, text=f"Total Fare : {tf} taka.", border=0,bg='white', fg='Black', font='roboto 12 bold').place(x=90, y=300)

    def con():
        tkinter.messagebox.showinfo("Payment Confirmation", "Payment Successful!!")
        Label(window, text=f"Thank You for Your Payment", border=0, bg='white', fg='Black',
              font='roboto 12 bold').place(x=70, y=400)
        Button(window, text="Show Ticket", relief=GROOVE, bg='Yellow', fg='Black',font='roboto 12 bold',command=lambda: goto()).place(x=120, y=500)

    def goto():
        window.quit()
        page_7()

    # running main loop
    window.mainloop()

def page_7():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    global bs

    global tf

    global bus_no
    global time

    # BG Image
    Label(window, image=tk_bg, border=0).place(x=0, y=0)
    Label(window, text=f"{bus_no}", border=0, bg='white', fg='Black',
          font='roboto 12 bold').place(x=70, y=130)
    Label(window, text=f"Destination : {sd}-{fd}", border=0, bg='white', fg='Black',
          font='roboto 10 bold').place(x=70, y=160)
    Label(window, text=f"Time : {time}", border=0, bg='white', fg='Black',
          font='roboto 10 bold').place(x=70, y=190)
    Label(window, text=f"Seat No :", border=0, bg='white', fg='Black',
          font='roboto 10 bold').place(x=70, y=220)
    ct=1
    for x in bs:
        Label(window, text=x, bg='white', fg='Black',font='roboto 10 bold').place(x=110 + (20 * ct), y=218)
        ct+=1

    Label(window, text=f"Total fare paid : {tf} Taka", border=0, bg='white', fg='Black',
          font='roboto 10 bold').place(x=70, y=250)
    Button(window, text='Cancel Ticket', relief=GROOVE, bg='#AFA6F9', fg='Black',
           font='roboto 8 bold', command=lambda: cn_pg()).place(x=250, y=270)

    Button(window, text='Book Another Ticket', relief=GROOVE, bg='#AFA6F9',fg='Black',
          font='roboto 12 bold', command=lambda: nt_pg(), width=20).place(x=80,y=500)
    Button(window, text='Exit', relief=GROOVE, bg='#AFA6F9',fg='Black',
          font='roboto 12 bold', command=lambda: exit(), width=20).place(x=80,y=550)

    def cn_pg():
        window.quit()
        page_8()
    def nt_pg():
        window.quit()
        page_4()
    def exit():
        window.destroy()

    # running main loop
    window.mainloop()
def page_8():
    window.title("bRider")
    # Adjust size
    window.geometry("360x640")

    global tf
    global sd
    global fd
    global bus_no


    # BG Image
    Label(window, image=cn_bg, border=0).place(x=0, y=0)
    Label(window, text=f"Refundable Amount = {tf*0.7} Taka", border=0, bg='white', fg='Black',
          font='roboto 11 bold').place(x=80, y=220)
    Label(window, text=f"{sd}", border=0, bg='white', fg='Black',
          font='roboto 8 bold').place(x=50, y=135)
    Label(window, text=f"{fd}", border=0, bg='white', fg='Black',
          font='roboto 8 bold').place(x=240, y=135)
    Label(window, text=f"{bus_no}", border=0, bg='white', fg='Black',
          font='roboto 11 bold').place(x=140, y=120)
    Button(window, image=cn_bt, relief=GROOVE, bg='white', border=0,
           command=lambda: exit()).place(x=40, y=500)

    def exit():
        tkinter.messagebox.showinfo("Ticket Cancel","Your Ticket has cancelled")
        window.destroy()

    # running main loop
    window.mainloop()

if __name__ == '__main__':
    front()


