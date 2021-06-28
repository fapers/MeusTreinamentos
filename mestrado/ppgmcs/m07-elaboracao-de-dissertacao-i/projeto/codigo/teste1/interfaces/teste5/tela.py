'''
https://www.youtube.com/channel/UCm63tB8wsKOVvxoU4iMpS2A
'''
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # sg.theme_previewer()
        # sg.theme('Reddit')
        sg.change_look_and_feel('Default')
        # Layout
        layout = [
            [sg.Text('Nome:'), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade:'), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],

            [sg.Checkbox('Gmail:', key='gmail'),
             sg.Checkbox('Outlook', key='outlook'),
             sg.Checkbox('Yahoo', key='yahoo')],

            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'),
             sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],

            [sg.Slider(range=(0, 255), default_value=0, orientation='h',
                       size=(15, 20), key='sliderVelocidade')],

            [sg.Button('Enviar Dados')],

            [sg.Output(size=(30, 20))]
        ]

        # Janela
        self.janela1 = sg.Window('Dados pessoais').layout(layout)

        # Extrair os dados da tela
        # self.button, self.values = self.janela1.Read()

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela1.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não aceita Cartão: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')
            print('------------')


tela = TelaPython()
tela.Iniciar()
