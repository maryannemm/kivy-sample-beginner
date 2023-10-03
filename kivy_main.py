from kivy.app import App #incharge of the graphics  inherited by myapp. run() is configured automatically
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class Users(Widget):
    #assign text field values from names to the following 
    username=ObjectProperty(None)
    email=ObjectProperty(None)
    password=ObjectProperty(None)
    why=ObjectProperty(None)
    
    #function for the button
    def btn(self):
        print(f'your user name is: {self.username.text} and your email is {self.email.text} and your password is {self.password.text} your why {self.why.text}')
        self.username.text=""
        self.password.text=""
        self.email.text=""
        self.why.text=""


class Myapllication(App):
    def build(self):
        Builder.load_file("myapplication.kv") 
        return Users()

if __name__=="__main__":
    Myapllication().run()
