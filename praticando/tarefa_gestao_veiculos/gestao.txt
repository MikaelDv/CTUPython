from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config

class SistemaLojaVeiculos(App):

    carros = []

    carro_atual = None

    txt_marca = TextInput()
    txt_modelo = TextInput()
    txt_ano = TextInput()
    txt_placa = TextInput()

    def __init__(self):
        App.__init__(self)
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


    def salvar(self, e):
        obj_carro = {"marca": self.txt_marca.text,
                       "modelo": self.txt_modelo.text,
                       "ano": self.txt_ano.text,
                       "placa": self.txt_placa.text}
        if self.carro_atual is not None:
            self.carros.remove(self.carro_atual)
            self.carro_atual = None
        self.carros.append( obj_carro )
        self.txt_marca.text = ""
        self.txt_modelo.text = ""
        self.txt_ano.text = ""
        self.txt_placa.text = ""
        print(self.carros)


    def pesquisar(self, e):
        for carro in self.carros:
            if self.txt_placa.text.lower() in carro["placa"].lower():
                self.carro_atual = carro
                self.txt_marca.text = carro["marca"]
                self.txt_modelo.text = carro["modelo"]
                self.txt_ano.text = carro["ano"]
                self.txt_placa.text = carro["placa"]


    def build(self):
        box_marca = BoxLayout(orientation="horizontal", padding=5)
        lbl_marca = Label(text="Marca:", size_hint=(0.7,1))
        box_marca.add_widget(lbl_marca)
        box_marca.add_widget(self.txt_marca)

        box_modelo = BoxLayout(orientation="horizontal", padding=5)
        lbl_modelo = Label(text="Modelo:", size_hint=(0.7,1))
        box_modelo.add_widget(lbl_modelo)
        box_modelo.add_widget(self.txt_modelo)

        box_ano = BoxLayout(orientation="horizontal", padding=5)
        lbl_ano = Label(text="Ano:", size_hint=(0.7,1))
        box_ano.add_widget(lbl_ano)
        box_ano.add_widget(self.txt_ano)

        box_placa = BoxLayout(orientation="horizontal", padding=5)
        lbl_placa = Label(text="Placa:", size_hint=(0.7,1))
        box_placa.add_widget(lbl_placa)
        box_placa.add_widget(self.txt_placa)

        box_botoes = BoxLayout(orientation="horizontal", padding=5)
        btn_salvar = Button(text="Salvar", on_release=self.salvar)
        btn_pesquisar = Button(text="Pesquisar", on_release=self.pesquisar)
        box_botoes.add_widget(btn_salvar)
        box_botoes.add_widget(btn_pesquisar)

        box_geral = BoxLayout(orientation="vertical")
        box_geral.add_widget(box_marca)
        box_geral.add_widget(box_modelo)
        box_geral.add_widget(box_ano)
        box_geral.add_widget(box_placa)
        box_geral.add_widget(box_botoes)
        
        return box_geral

if __name__ == "__main__":
    Window.size = (500,200)
    SistemaLojaVeiculos().run()