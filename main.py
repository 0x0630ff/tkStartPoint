from tkinter import *
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
main_button_width = 32
main_button_height = 2
quit_red = '#cc0c13'
default_button_color = '#ff00ff'
lightbluebg = '#d8e4e6'
gray0 = '#cdbed1'
gray1 = '#ac9eb0'
gray2 = '#222222'
gray3 = '#303030'

mainbg = gray1

def tossit(inputtext=None):
    print('tossed.', inputtext)

def startvalor_append():
    startvalor()
    app.lift()


class Splash(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Splash Screen')
        self.label = Label(self, text="SPLASH")
        self.lift()


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self, default="assets\\hammer.ico")
        Tk.wm_title(self, "DFM Tool")
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        APP_FRAMES = (  StartPage,
                        PageOne,
                        PageTwo,
                        PageThree,
                        )

        self.frames = dict()
        self.add_frames(container, APP_FRAMES)
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def add_frames(self, container, FrameSet):
        for F in FrameSet:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


# to make a new page, 
# define as a class similar to below 
# then add the class to the list 
# of classes in the self.add_frames() method.

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background=mainbg)
        label = Label(self, text="WELCOME | START PAGE", font=LARGE_FONT, bg=mainbg, fg='white')
        label.pack(padx=10, pady=10)
        setup_shared_buttons(self, controller)

class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background=mainbg)
        label = Label(self, text="Open Valor", font=LARGE_FONT, bg=mainbg, fg='white')
        label.pack(padx=10, pady=10)
        setup_shared_buttons(self, controller)
        open_valor_button = Button(self, text="Do A Thing!", 
                                    command=startvalor_append, 
                                    width=main_button_width,
                                    height=main_button_height,
                                    bg=lightbluebg,
                                    )
        open_valor_button.pack(padx=10, pady=10, side=RIGHT, fill=BOTH, expand=False)


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background=mainbg)
        label = Label(self, text="Close Valor", font=LARGE_FONT, bg=mainbg, fg='white')
        label.pack(padx=10, pady=10)
        setup_shared_buttons(self, controller)


class PageThree(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, background=mainbg)
        label = Label(self, text="Open A Job", font=LARGE_FONT, bg=mainbg, fg='white')
        label.pack(padx=10, pady=10)
        setup_shared_buttons(self, controller)


# for adding all the buttons to navigate
def setup_shared_buttons(self, controller):
    main_page_button = Button(  self, text = "MAIN PAGE", 
                                command = lambda: controller.show_frame(StartPage), 
                                width = main_button_width,
                                height = main_button_height,
                                bg = lightbluebg,   )

    main_page_button.pack(  padx=10, pady=10, side=TOP, fill=BOTH, expand=True  )

    button1 = Button(   self, text = "1 - Open Valor", 
                        command = lambda: controller.show_frame(PageOne), 
                        width = main_button_width,
                        height = main_button_height,    )

    button1.pack(   padx=10, pady=10, side=TOP, fill=BOTH, expand=True  )

    button2 = Button(   self, text = "2 - Close Valor", 
                        command = lambda: controller.show_frame(PageTwo), 
                        width = main_button_width,
                        height = main_button_height,    )

    button2.pack(   padx=10, pady=10, side=TOP, fill=BOTH, expand=True  )
    
    button3 = Button(   self, text="3 - Open A Job", 
                        command = lambda: controller.show_frame(OpenJob), 
                        width = main_button_width,
                        height = main_button_height,    )

    button3.pack(   padx=10, pady=10, side=TOP, fill=BOTH, expand=True  )
    
    button4 = Button(   self, text="4 - Import New Job", 
                        command = lambda: controller.show_frame(PageThree), 
                        width = main_button_width,
                        height = main_button_height,    )

    button4.pack(   padx=10, pady=10, side=TOP, fill=BOTH, expand=True  )
    
    quit_button = Button(   self, text = "Quit", 
                            command = lambda: quit(), 
                            width = main_button_width,
                            height = main_button_height,
                            bg = quit_red,  )

    quit_button.pack(   padx=10, pady=10, side=TOP, fill=BOTH, expand=True )


app = MainApp()
app.attributes("-topmost", True)  # keeps window on top of all other windows
app.mainloop()
