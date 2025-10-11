from customtkinter import *
from back_end import *



# front_end part
class Calculator_visuals_advanced(CTk):
    def __init__(self, back_to_main):
        super().__init__()
        self.back_to_main = back_to_main
        self.title("Calculator")
        self.geometry("550x750")
        self.font = ("Comic Sans MS", 50, "bold")
        self.ENTRY_FONT = ("Comic Sans MS", 20, "bold")
        self.bind_all("<Key>", self.key_pressed)

        # Entry_Frame
        self.ENTRY_FRAME = CTkFrame(self, width=550, height=450, corner_radius=16)
        self.ENTRY_FRAME.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.ENTRY_FRAME.grid_columnconfigure(0, weight=1)

        # Entry
        self.ENTRY = CTkEntry(self.ENTRY_FRAME, width=500, height=75, corner_radius=16, fg_color="black",
                              placeholder_text=("0"), font=self.ENTRY_FONT)
        self.ENTRY.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Button_Frame
        self.FRAME = CTkFrame(self, width=550, height=550, corner_radius=16, fg_color="black")
        self.FRAME.grid(row=1, column=0, pady=10, padx=15)

        buttons = [
            ["1", "2", "3", "/", ")", "C"],
            ["4", "5", "6", "*", "(", "⌫"],
            ["7", "8", "9", "-", "ANS", "="],
            ["0", ".", ",", "^", "+", "pi"],
            ["e", "sin", "cos", "tan", "log", "sqrt"]
        ]


        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                CTkButton(self.FRAME, text=char, width=80, height=80, fg_color="gray", corner_radius=16, font=(("Comic Sans MS", 20, "bold")),
                          command=lambda ch=char: handle_click(ch, self.ENTRY)).grid(row=r, column=c, padx=2, pady=2)

                self.BUTTON_BACK_TO_BASIC = CTkButton(self, width=300, height=150, corner_radius=16, fg_color="gray",
                                                      text="Back to basic mode",
                                                      font=("Comic Sans MS", 18, "bold"),
                                                      command=self.back_to_main
                                                      )
                self.BUTTON_BACK_TO_BASIC.grid(row=2, column=0, padx=5, pady=5)

    def key_pressed(self, event):
        key = event.char

        allowed_keys = "0123456789+-*/().^,"
        if key in allowed_keys:
            handle_click(key, self.ENTRY)
        elif key == "\r":  # Enter
            handle_click("=", self.ENTRY)
        elif key == "\x08":  # Backspace
            handle_click("⌫", self.ENTRY)
        elif key.lower() == "c":
            handle_click("C", self.ENTRY)

