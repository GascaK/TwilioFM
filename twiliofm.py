from tkinter import *
from tkinter import ttk
from make_call import Call
import re
import os


class TwilioFM(Tk):
    ''' Main entry point for project

        Window handler and information logic behind the
        Twilio File Maker app.
    '''

    VERSION = 0.9

    def __init__(self):
        ''' TwilioFM main entry point, no parameters

        TwilioFM takes in any string copied to the users
        keyboard and sanitizes it for viable phone number.
        Then utilizing Twilio's API Rest architecture
        dials that number and the users personal telephone.
        '''

        super().__init__()
        self.title('Twilio FM v.{}'.format(self.VERSION))
        self.geometry('{}x{}'.format(220, 75))
        self.resizable(False, False)
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0)
        self.results = IntVar()
        self.clipboard_clear()
        ###########################
        #    TTK Button artwork   #
        b = ttk.Button(self.frame,
                       text='Call Number',
                       width='20',
                       command=lambda: self.make_call(digits))
        b.grid(column=0, row=1, columnspan=3)
        ###########################
        self.show_menu()
        self.update()

        while True:
            # Checks keyboard input for valid telephone.
            # prevents error if NULL.
            try:
                digits = self.extract_number(self.clipboard_get())
            except TclError:
                digits = 'Copy a valid 11 digit Phone Number'
            self.show_number(digits)
            self.update()

    def show_number(self, number):
        ###########################
        #    TTK Label Artwork    #
        label = ttk.Label(self.frame,
                          width='35',
                          anchor=CENTER,
                          text=str(number))
        label.grid(column=0, row=0, columnspan=3)
        ###########################
        label['textvariable'] = self.results
        self.results.set(number)

    def show_menu(self):
        # Create Menu Items #
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open Config',
                             command=self.open_tfmp)
        filemenu.add_command(label='Close',
                             command=self.destroy)
        menubar.add_cascade(label='File', menu=filemenu)
        self.config(menu=menubar)

    def open_tfmp(self):
        # Opens tfmp in default text editor
        os.startfile('src\\tfmp.ini')

    def extract_number(self, copied_string):
        # Extract 11 digit number from copied_string and returns string.
        number = re.findall('[0-9]', copied_string)
        if len(number) == 11:
            return '+{}'.format(''.join(number))
        elif len(number) == 10:
            return '+1{}'.format(''.join(number))
        else:
            return

    def make_call(self, valid_number):
        # Create instance object of Call and dials valid_number
        call = Call()
        call.dial_phone(valid_number)


if __name__ == '__main__':
    tfmp = TwilioFM()
