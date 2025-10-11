from customtkinter import *
from back_end import *



#front_end part
class Calculator_visuals(CTk):
    def __init__(self, switch_to_advanced):
        super().__init__()
        self.switch_to_advanced = switch_to_advanced
        self.title("Calculator")
        self.geometry("550x750")
        self.font = ("Comic Sans MS", 50, "bold")
        self.ENTRY_FONT = ("Comic Sans MS", 20, "bold")
        self.bind_all("<Key>", self.key_pressed)

        #Entry_Frame
        self.ENTRY_FRAME = CTkFrame(self, width = 550, height=450, corner_radius= 16)
        self.ENTRY_FRAME.grid(row=0, column=0, pady=10, padx=10)
        self.ENTRY_FRAME.grid_columnconfigure(0, weight=1)

        #Entry
        self.ENTRY = CTkEntry(self.ENTRY_FRAME, width = 355, height= 75, corner_radius= 16, fg_color= "black", placeholder_text=("0"), font=self.ENTRY_FONT)
        self.ENTRY.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="we")
        
        #Button_Frame
        self.FRAME = CTkFrame(self, width = 550, height=450, corner_radius= 16, fg_color= "black")
        self.FRAME.grid(row=1, column=0, pady=10, padx = 15)

        #Button_1
        self.BUTTON1 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray", text="1", font=self.font, command=lambda: handle_click("1", self.ENTRY))
        self.BUTTON1.grid(row=1, column=0, padx=5, pady = 5)

        #Button_2
        self.BUTTON2 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="2",font=self.font, command=lambda: handle_click("2", self.ENTRY))
        self.BUTTON2.grid(row=1, column=1, padx=5, pady = 5)

        #Button_3
        self.BUTTON3 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="3",font=self.font, command=lambda: handle_click("3", self.ENTRY))
        self.BUTTON3.grid(row=1, column=2, padx=5, pady = 5)

        #Button_4
        self.BUTTON4 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="4",font=self.font, command=lambda: handle_click("4", self.ENTRY))
        self.BUTTON4.grid(row=2, column=0, padx=5, pady = 5)

        #Button_5
        self.BUTTON5 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="5",font=self.font, command=lambda: handle_click("5", self.ENTRY))
        self.BUTTON5.grid(row=2, column=1, padx=5, pady = 5)

        #Button_6
        self.BUTTON6 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="6",font=self.font, command=lambda: handle_click("6", self.ENTRY))
        self.BUTTON6.grid(row=2, column=2, padx=5, pady = 5)

        #Button_7
        self.BUTTON7 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="7",font=self.font, command=lambda: handle_click("7", self.ENTRY))
        self.BUTTON7.grid(row=3, column=0, padx=5, pady = 5)

        #Button_8
        self.BUTTON8 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="8",font=self.font, command=lambda: handle_click("8", self.ENTRY))
        self.BUTTON8.grid(row=3, column=1, padx=5, pady = 5)

        #Button_9
        self.BUTTON9 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="9",font=self.font, command=lambda: handle_click("9", self.ENTRY))
        self.BUTTON9.grid(row=3, column=2, padx=5, pady = 5)

        #Button_0
        self.BUTTON0 = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="0",font=self.font, command=lambda: handle_click("0", self.ENTRY))
        self.BUTTON0.grid(row=4, column=1, padx=5, pady = 5)

        #Button_C
        self.BUTTONC = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="C",font=self.font, command=lambda: handle_click("C", self.ENTRY))
        self.BUTTONC.grid(row=4, column=0, padx=5, pady = 5)

        #OPERATORS
        #Button_,
        self.BUTTON = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text=".",font=self.font, command=lambda: handle_click(".", self.ENTRY))
        self.BUTTON.grid(row=4, column=2, padx=5, pady = 5)

        #Button_/
        self.BUTTON_DIV = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="/",font=self.font, command=lambda: handle_click("/", self.ENTRY))
        self.BUTTON_DIV.grid(row=1, column=3, padx=5, pady = 5)

        #Button_*
        self.BUTTON_MULTY = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="*",font=self.font, command=lambda: handle_click("*", self.ENTRY))
        self.BUTTON_MULTY.grid(row=2, column=3, padx=5, pady = 5)

        #Button_+
        self.BUTTON_ADD = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="+",font=self.font, command=lambda: handle_click("+", self.ENTRY))
        self.BUTTON_ADD.grid(row=3, column=3, padx=5, pady = 5)

        #Button_-
        self.BUTTON_MIN = CTkButton(self.FRAME, width = 100, height=100, corner_radius= 16, fg_color= "gray",text="-",font=self.font, command=lambda: handle_click("-", self.ENTRY))
        self.BUTTON_MIN.grid(row=4, column=3, padx=5, pady = 5)


        #ENTRY_BUTTONS
        #Button_⌫
        self.BUTTON_BACK = CTkButton(self.ENTRY_FRAME, width=50, height=60, corner_radius=16,
                                     fg_color="grey22", text="⌫", font=self.ENTRY_FONT, text_color="red", command=lambda: handle_click("⌫", self.ENTRY))
        self.BUTTON_BACK.grid(row=0, column=4, padx=5, pady=5, sticky="e")

        #Button_=
        self.BUTTON_EQ = CTkButton(self.ENTRY_FRAME, width=50, height=60, corner_radius=16,
                                   fg_color="grey22", text="=", font=self.ENTRY_FONT, text_color="cyan", command=lambda: handle_click("=", self.ENTRY))
        self.BUTTON_EQ.grid(row=0, column=0, padx=5, pady=5,)

        #ADVANCED_BUTTON
        # Button_OPTION
        self.BUTTON_ADV = CTkButton(self, width=300, height=100, corner_radius=16, fg_color="gray", text="Switch to advanced mode ",
                                 font = (("Comic Sans MS", 18, "bold")),
                                    command = self.switch_to_advanced)

        self.BUTTON_ADV.grid(row=2, column=0, padx=5, pady=5)

    def key_pressed(self, event):
        key = event.char

        # Перевірка на допустимі символи
        allowed_keys = "0123456789+-*/().^,"
        if key in allowed_keys:
            handle_click(key, self.ENTRY)
        elif key == "\r":  # Enter
            handle_click("=", self.ENTRY)
        elif key == "\x08":  # Backspace
            handle_click("⌫", self.ENTRY)
        elif key.lower() == "c":
            handle_click("C", self.ENTRY)
