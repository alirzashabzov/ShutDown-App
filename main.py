from tkinter import*
import os 

root=Tk()
root.title('Shutdown App')
root.geometry('400x580')
root.configure(bg="#fff")
root.resizable(False, False)


def restarttime():
    os.system('shutdown /r /t 30')

def restart():
    os.system('shutdown /r /t 1')

def shutdown():
    os.system('shutdown /s /t 1')

def logout():
    os.system('shutdown -l')






# icon
image_icon = PhotoImage(file='image/restart time.png')
root.iconphoto(False, image_icon)


#first button
restart_time_button=PhotoImage(file='image/restart time.png')
first_button=Button(root,image=restart_time_button,
borderwidth=0,cursor='hand2', command=restarttime)
first_button.place(x=10,y=10)

#second button
close_button = PhotoImage(file='image/close.png')
second_button = Button(root, image=close_button,
                      borderwidth=0, cursor='hand2',
                      command=root.destroy)
second_button.place(x=200, y=10)


# third button
restart_button = PhotoImage(file='image/restart.png')
third_button = Button(root, image=restart_button,
                       borderwidth=0, cursor='hand2',
                       command=restart)
third_button.place(x=10,y=200)


#fouth button
shutdown_button = PhotoImage(file='image/shutdown.png')
fouth_button = Button(root, image=shutdown_button,
                       borderwidth=0, cursor='hand2',
                      command= shutdown)
fouth_button.place(x=200, y=200)


# fifth button
logout_button = PhotoImage(file='image/log out.png')
fifth_button = Button(root, image=logout_button,
                      borderwidth=0, cursor='hand2',
                      command=logout)
fifth_button.place(x=10, y=400)








root.mainloop()










