from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
 
 
 
class MyApp(App):
     def build(self):
        txt = Label(text = 'this is text!!!')
        btn = Button(txt)
        layout = BoxLayout(txt)
        layout.add_widget(txt)
        return layout
MyApp().run()