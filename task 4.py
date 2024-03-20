from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        self.txt = Label(text = "this is text")
        btn = Button(text = "this is button!")
        btn.on_press = self.change_text
        layout= BoxLayout()
        layout.add_widget(self.txt)
        layout.add_windet(btn)
        return layout
        
    def change_text(self):
        self.txt.text = str(self.i)
        self.i += 1





MyApp().run()            