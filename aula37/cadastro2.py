from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config

class Agenda(App):

    agenda = []

    contato_atual = None

    txt_nome = TextInput()
    txt_telefone = TextInput()
    txt_email = TextInput()
    txt_nascimento = TextInput()

    def __init__(self):
        App.__init__(self)
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


    def salvar(self, e):
        obj_contato = {"nome": self.txt_nome.text,
                       "telefone": self.txt_telefone.text,
                       "email": self.txt_email.text,
                       "nascimento": self.txt_nascimento.text}
        if self.contato_atual is not None:
            self.agenda.remove(self.contato_atual)
            self.contato_atual = None
        self.agenda.append( obj_contato )
        self.txt_nome.text = ""
        self.txt_telefone.text = ""
        self.txt_email.text = ""
        self.txt_nascimento.text = ""
        print(self.agenda)


    def pesquisar(self, e):
        for contato in self.agenda:
            if self.txt_nome.text.lower() in contato["nome"].lower():
                self.contato_atual = contato
                self.txt_nome.text = contato["nome"]
                self.txt_telefone.text = contato["telefone"]
                self.txt_email.text = contato["email"]
                self.txt_nascimento.text = contato["nascimento"]


    def build(self):
        box_nome = BoxLayout(orientation="horizontal", padding=5)
        lbl_nome = Label(text="Nome:", size_hint=(0.7,1))
        box_nome.add_widget(lbl_nome)
        box_nome.add_widget(self.txt_nome)

        box_telefone = BoxLayout(orientation="horizontal", padding=5)
        lbl_telefone = Label(text="Telefone:", size_hint=(0.7,1))
        box_telefone.add_widget(lbl_telefone)
        box_telefone.add_widget(self.txt_telefone)

        box_email = BoxLayout(orientation="horizontal", padding=5)
        lbl_email = Label(text="Email:", size_hint=(0.7,1))
        box_email.add_widget(lbl_email)
        box_email.add_widget(self.txt_email)

        box_nascimento = BoxLayout(orientation="horizontal", padding=5)
        lbl_nascimento = Label(text="Nascimento:", size_hint=(0.7,1))
        box_nascimento.add_widget(lbl_nascimento)
        box_nascimento.add_widget(self.txt_nascimento)

        box_botoes = BoxLayout(orientation="horizontal", padding=5)
        btn_salvar = Button(text="Salvar", on_release=self.salvar)
        btn_pesquisar = Button(text="Pesquisar", on_release=self.pesquisar)
        box_botoes.add_widget(btn_salvar)
        box_botoes.add_widget(btn_pesquisar)

        box_geral = BoxLayout(orientation="vertical")
        box_geral.add_widget(box_nome)
        box_geral.add_widget(box_telefone)
        box_geral.add_widget(box_email)
        box_geral.add_widget(box_nascimento)
        box_geral.add_widget(box_botoes)
        
        return box_geral

if __name__ == "__main__":
    Window.size = (500,200)
    Agenda().run()