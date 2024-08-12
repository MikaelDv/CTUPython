from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Formulario(App):
    def build(self):
        box_nome = BoxLayout(orientation="horizontal", padding=5)
        lbl_nome = Label(text="Nome:")
        txt_nome = TextInput()
        box_nome.add_widget(lbl_nome)
        box_nome.add_widget(txt_nome)

        box_telefone = BoxLayout(orientation="horizontal", padding=5)
        lbl_telefone = Label(text="Telefone:")
        txt_telefone = TextInput()
        box_telefone.add_widget(lbl_telefone)
        box_telefone.add_widget(txt_telefone)

        box_email = BoxLayout(orientation="horizontal", padding=5)
        lbl_email = Label(text="Email:")
        txt_email = TextInput()
        box_email.add_widget(lbl_email)
        box_email.add_widget(txt_email)

        box_botoes = BoxLayout(orientation="horizontal", padding=5)
        btn_salvar = Button(text="Salvar")
        btn_pesquisar = Button(text="Pesquisar")
        box_botoes.add_widget(btn_salvar)
        box_botoes.add_widget(btn_pesquisar)

        box_geral = BoxLayout(orientation="vertical")
        box_geral.add_widget(box_nome)
        box_geral.add_widget(box_telefone)
        box_geral.add_widget(box_email)
        box_geral.add_widget(box_botoes)
        
        return box_geral

if __name__ == "__main__":
    Window.size = (400,200)
    Formulario().run()