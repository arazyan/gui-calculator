import tkinter as tk

SMALL_FONT_STYLE    = ("Arial", 16)
LARGE_FONT_STYLE    = ("Arial", 30, "bold")
DIGIT_FONT_STYLE    = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE  = ("Arial", 20)

OFF_WHITE   = "#F8FAFF"
WHITE       = "#FFFFFF"
LIGHT_BLUE  = "#CCEDFF"
LIGHT_GRAY  = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    # init main window
    def __init__(self):
        self.window = tk.Tk()
        # size of a standart resolution on iphone 8
        self.window.geometry('750x1334')
        # disable resizing for window
        self.window.resizable(0,0)
        # set a title in title bar
        self.window.title('Advanced Calculator')
        
        # set display labels for expressions
        self.total_expression = ''
        self.current_expression = ''
	
		# set frame and label settings
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            # number : (row, col)
            7 : (1, 1), 8 : (1, 2), 9 : (1, 3),  
            4 : (2, 1), 5 : (2, 2), 6 : (2, 3),  
            1 : (3, 1), 2 : (3, 2), 3 : (3, 3),  
            0 : (4, 2), '.' : (4, 1)
        }

        self.operations = {"/": "\u00F7", "*" : "\u00D7", "-" : "-", "+" : "+"}

        # expand the workspace area
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        # set digit buttons
        self.create_digit_buttons()
        # set operation buttons
        self.create_operator_buttons()
        # set resultant buttons
        self.create_special_buttons()
        # set keyboard input
        self.bind_keys()


    def create_display_labels(self):
        """
                N
            W       E
                S
        """
        total_label = tk.Label(self.display_frame, text=self.total_expression, 
							   anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR,
							   padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, 
                               anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, 
                               padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label


    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame


    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame


    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, 
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, 
                               fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=OFF_WHITE, 
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, 
                            borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
        

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=LIGHT_BLUE, 
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, 
                            borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=1, sticky=tk.NSEW)

    
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=LIGHT_BLUE, 
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, 
                            borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)


    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=LIGHT_BLUE, 
                            fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, 
                            borderwidth=0, command=self.square_root)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),
                             lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(str(key),
                             lambda event, operator=key: self.append_operator(operator))


    def create_special_buttons(self):
        self.create_equals_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_square_root_button()


    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()


    def square_root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()


    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_label()
        self.update_label()


    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_total_label()
        self.update_label()


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression=''
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()


    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()


    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)


    def update_label(self):
        self.label.config(text=self.current_expression[:10])


    # run our app
    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()

