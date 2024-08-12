from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Calculadora(App):
    def build(self):
        boxGeral = BoxLayout(orientation="vertical")
        box1 = BoxLayout(orientation="horizontal")
        lbl_numero1 = Label(text="Digite o 1° número:")
        txt_numero1 = TextInput(font_size="50")
        box2 = BoxLayout(orientation="horizontal")
        lbl_numero2 = Label(text="Digite o 2° número:")
        txt_numero2 = TextInput(font_size="50")
        btn_somar = Button(text="somar")
        box1.add_widget(lbl_numero1)
        box1.add_widget(txt_numero1)
        box2.add_widget(lbl_numero2)
        box2.add_widget(txt_numero2)
        boxGeral.add_widget(box1)
        boxGeral.add_widget(box2)
        boxGeral.add_widget(btn_somar)
        return boxGeral

if __name__ == "__main__":
    Calculadora().run()