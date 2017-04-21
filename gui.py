# Author's name:            Lukas Mohs
# Creation Date:            04/18/17
# Last Modification Date:   04/18/17
# Brief Description:
#
# This GUI application provides a simple property tax calculator
# that takes the property value in USD as an input,
# calculates and displays the assessment value as an intermediate step
# and finally displays the property tax in USD. A text field provides
# the interface to enter the property value, meanwhile the "Calcualte"
# button triggers the actual calculation. Additionally, a "Exit" button
# is provided to end the application.

import tkinter
import tkinter.messagebox

# This class implements all the functionality to create and display
# the GUI that enables user interaction. The UI is divided into three
# frames where the first one holds a heading as well as the labeled input
# field. The one in the middle contains the intermediate and final
# calculation result. The bottom frame contains both buttons to trigger
# the calculation and the exit the program.
class TaxCalculatorGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.heading_label = tkinter.Label(self.top_frame, \
                    text='Property Tax Calculator')
        self.heading_label.config(font=("Courier", 20))
        self.prompt_label = tkinter.Label(self.top_frame, \
                    text='Enter the value of a property in $:')
        self.property_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.heading_label.pack(fill='x')
        self.prompt_label.pack(side='left')
        self.property_entry.pack(side='left')

        # Create the widgets for the center frame
        self.assessment_label = tkinter.Label(self.middle_frame, \
                    text='assessment value: 0$')
        self.tax_label = tkinter.Label(self.middle_frame, \
                    text='property tax: 0$')

        # Pack the center frame's widgets
        self.assessment_label.pack(fill='x')
        self.tax_label.pack(fill='x')

        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, \
                    text="Calculate", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                    text="Exit", command=self.main_window.destroy)
        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        # Enter tkinter the main loop
        tkinter.mainloop()

    # The calculate method is a callback function for the Calculate button
    def calculate(self):
        # Get the value entered by the user and convert to float
        try:
            propertyValue = float(self.property_entry.get())
        except:
            # Display an error message in case it couldn't be converted
            tkinter.messagebox.showinfo("Error","Please input a number!")
        
        # Calculate the assessment value
        assessmentValue = propertyValue * 0.6
        
        # Calculate the tax
        tax = assessmentValue * 0.0075
        
        # Display the results in both text labels
        self.assessment_label.config(text="assessment value: " \
                                     + str(assessmentValue) + "$")
        self.tax_label.config(text="property tax: " + str(tax) + "$")

# Create an instance of the TaxCalculatorGUI class
tax_calulator = TaxCalculatorGUI()
