from PySimpleGUI import PySimpleGUI as sg
import gtts
from playsound import playsound
import os



# Layout da janela
sg.theme = 'Dark Blue 3'
layout = [
  [sg.Text('Digite oque deve ser falado:')],
  [sg.Multiline(key='message', size=(50,8))],
  [sg.Button('Speak')],
  [sg.Checkbox('Escolher um arquivo .txt', default=False, key='arq', enable_events=True), sg.Input(size=(30,1), key='-File-', disabled=True), sg.FileBrowse('Browse', disabled=True)],
]

# Janela
janela = sg.Window('Speak Text', layout)


# Arquivos e variaveis
audio_path_file = 'D:/Estudos/Programação/Projetos/FalaPython/frase.mp3'
check_box = False

'''

'r' - > Usado para somente ler algo
'w' - > Usado somente para escrever algo
'r+ - > Usado para ler e escrever algo
'a' - > Usado para acrescentar algo

'''
def delete_path_files():
  if os.path.exists('speak.txt'):
    os.remove('speak.txt')
  if os.path.exists('frase.mp3'):
    os.remove('frase.mp3')
 
def path_file(text):
  if text != '':
    with open(text, 'r', encoding='utf-8') as arquivo:
      if arquivo != '':
        for linha in arquivo:
          frase = gtts.gTTS(linha, lang='pt-br')
          frase.save('D:/Estudos/Programação/Projetos/FalaPython/frase.mp3')
          playsound('frase.mp3')
      else:
        erro() 
  else:
      erro()
  

def checkbox(check_box):
  if check_box:
    janela['Browse'].update(disabled=False)
    janela['message'].update('',disabled=True)
  else:
    janela['Browse'].update(disabled=True)
    janela['message'].update(disabled=False)
    janela['-File-'].update('')

def erro():
    sg.popup('[ERRO] O arquivo ou texto estão vazios ou inválidos.'
  '\nPor favor selecione um arquivo em formato .txt \nOu digite o texto!')
while True:
  events, value = janela.read()
      
  if events == sg.WINDOW_CLOSED:
    break
  if events == 'arq':
    check_box = value['arq']
    checkbox(check_box)
  if events == 'Speak':
    text = value['message']
    if check_box:
      path_file(value['-File-'])
    elif text != '':
      with open('speak.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(text)
      path_file('speak.txt')
    else:
      erro()
    
    delete_path_files()


