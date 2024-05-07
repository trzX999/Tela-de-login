from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Define a cor de fundo (cor cinza claro)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        # Adicionando a nova imagem de fundo
        self.add_widget(Image(source='nova_imagem_de_fundo.jpg'))

        # Layout para campos de entrada
        input_layout = BoxLayout(orientation='vertical', padding=8)

        self.add_widget(input_layout)

        input_layout.add_widget(Label(text='digite seu nome de usuário ', color=(0, 0, 0, 1)))

        # Campo de texto para o nome de usuário
        self.username = TextInput(hint_text='Nome de usuário', multiline=False, size_hint=(None, None), height=100,
                                  width=450)
        input_layout.add_widget(self.username)

        input_layout.add_widget(Label(text='digite sua senha ', color=(0, 0, 0, 1)))

        # Campo de texto para a senha
        self.password = TextInput(hint_text='Senha', multiline=False, password=True, size_hint=(None, None),
                                  height=100, width=450)
        input_layout.add_widget(self.password)

        # Layout para os botões
        button_layout = BoxLayout(padding=8)
        self.add_widget(button_layout)

        # Botão de login
        self.login_button = Button(text='Login', size_hint=(None, None), height=100, width=220)
        self.login_button.bind(on_press=self.login)
        button_layout.add_widget(self.login_button)

        # Botão de cadastro
        self.signup_button = Button(text='Cadastrar', size_hint=(None, None), height=100, width=220)
        self.signup_button.bind(on_press=self.signup)
        button_layout.add_widget(self.signup_button)

    def login(self, instance):
        # Lógica de autenticação aqui
        username = self.username.text
        password = self.password.text
        print(f'Tentativa de login com nome de usuário: {username} e senha: {password}')

    def signup(self, instance):
        # Lógica para ir para a tela de cadastro
        print('Abrir tela de cadastro')


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()