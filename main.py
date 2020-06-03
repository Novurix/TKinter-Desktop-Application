import tkinter as win

window = None
window_width = 1000
window_height = 720

def create_window():

    window = win.Tk()
    window.title("new Tkinter Window")

    canvas = win.Canvas(window, width=window_width, height=window_height)
    canvas.pack()
    main = win.Frame(window, bg="#000")
    main.place(relx=0,rely=0,relwidth=1,relheight=1)

    window.mainloop()

create_window()