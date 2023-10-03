from kivy.app import App #incharge of the graphics  inherited by myapp. run() is configured automatically
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

class Users(Widget):
    pass

class My_grid(GridLayout):
    def __init__(self, **kwargs):
        super(My_grid,self).__init__(*kwargs)
        self.cols = 1

        #these conditions apply to all the fields created below
        self.inside = GridLayout()  #to encapsulate all 'child' widgets
        self.add_widget(self.inside) #to encapsulate all 'child' widgets into a display
        self.inside.cols = 2
        self.inside.rows = 20

        #email field
        self.label=Label(text="E-mail: ", font_size=40) #label for the TextInput field
        self.email_input=TextInput(multiline=False)
        self.inside.add_widget(self.label)
        self.inside.add_widget(self.email_input)
        
        #First name field
        self.inside.add_widget(Label(text="First Name: ", font_size=40))
        self.first_name_input = TextInput (multiline=False)
        self.inside.add_widget(self.first_name_input)
        
        #last name field
        self.inside.add_widget(Label(text="Last Name: ", font_size=40))
        self.last_name_input = TextInput(multiline=False)
        self.inside.add_widget(self.last_name_input)

        #submit button
        self.submit_button = Button(text='Submit', font_size=100)
        self.submit_button.bind(on_press=self.clicked)
        self.add_widget(self.submit_button)
    #function to handle empty fields that maybe caught in the function below
    def show_popup(self, error_message):
        error_popup = Popup(title='Error message', size_hint=(None, None), size=(400, 200))
        error_label = Label(text=error_message)

        #cancel button
        cancel_button = Button(text="Cancel")
        cancel_button.bind(on_press=error_popup.dismiss)
        #error grid and layouts
        error_layout = GridLayout(cols=1)
        error_layout.add_widget(error_label)
        error_layout.add_widget(cancel_button)

        error_popup.content = error_layout
        error_popup.open()

    def clicked(self,*args):
        #grab the info typed in the text-fields, put them in variables and print them in the console
        email=self.email_input.text
        first=self.first_name_input.text
        last=self.last_name_input.text
        
        #veryify the data is not empty
        if not email:
            self.show_popup('Email cannot be empty')
        elif not first:
            self.show_popup('first name cannot be empty')
        elif not last:
            self.show_popup("Last name cannot be empty")
        else:
            print(f"your email is {email},your first name is {first},your last name is {last}")
        #clear the text fields
        self.email_input.text=""
        self.first_name_input.text=""
        self.last_name_input.text=""
class Myapllication(App):
    def build(self):
        return My_grid()

if __name__=="__main__":
    Myapllication().run()
