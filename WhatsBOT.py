import os
import configparser
import string
import pywhatkit
import keyboard
import time
import datetime
import win10toast
import colorama
from colorama import Fore, Style

cfg = configparser.ConfigParser()
cfg.read('CONFIGURACOES.ini')
tipo_msg = cfg.get('config','tipo_msg')
tempo = cfg.getint('config','tempo')
tempo_fechar = cfg.getint('config','tempo_fechar')
fechar = cfg.getboolean('config','fechar')

imagem = os.getcwd() + r'\img\imagem.jpeg'
icon = os.getcwd() + r'\img\whatsapp-icon.ico'

title_msg = 'WhatsBOT 0.1b'
time_msg = 15
cont = 0

with open('MENSAGEM.txt', 'r+') as mensagem:
    msg = ' '.join(mensagem.readlines())

with open('contatos.txt', 'r+', encoding='utf-8') as file:
    arq = file.read()

contatos = arq.split('\n')
n = win10toast.ToastNotifier()
colorama.init()
if fechar == True:
    n.show_toast(f'Configurações selecionadas '
    f'\nTipo de envio: {tipo_msg}'
    f'\nTempo para envio: {tempo}'
    f'\nFechar aba após o envio da mensagem? Sim'
    f'\nTempo para fechar a aba do WhatsApp Web: {tempo_fechar}')
    print(Fore.WHITE + Style.DIM + f'Configurações selecionadas'
          + Fore.GREEN + Style.DIM +
             f'\nTipo de envio: ' + Fore.WHITE + Style.DIM + f'{tipo_msg}'
          + Fore.GREEN + Style.DIM +
             f'\nTempo para envio: ' + Fore.WHITE + Style.DIM + f'{tempo}'
          + Fore.GREEN + Style.DIM +
             f'\nFechar aba após o envio da mensagem? ' + Fore.WHITE + Style.DIM + 'Sim'
        + Fore.GREEN + Style.DIM +
             f'\nTempo para fechar a aba do WhatsApp Web: ' + Fore.WHITE + Style.DIM + f'{tempo_fechar}')
else:
    n.show_toast(f'Configurações selecionadas'
                 f'\nTipo de envio: {tipo_msg}'
                 f'\nTempo para envio: {tempo}'
                 f'\nFechar aba após o envio da mensagem? Não'
                 f'\nTempo para fechar a aba do WhatsApp Web: {tempo_fechar}')
    print(Fore.GREEN + Style.DIM + f'Configurações selecionadas'
          + Fore.GREEN + Style.DIM +
          f'\nTipo de envio: ' + Fore.RED + Style.DIM + f'{tipo_msg}'
          + Fore.GREEN + Style.DIM +
          f'\nTempo para envio: ' + Fore.RED + Style.DIM + f'{tempo}'
          + Fore.GREEN + Style.DIM +
          f'\nFechar aba após o envio da mensagem? ' + Fore.RED + Style.DIM + 'Não'
          + Fore.GREEN + Style.DIM +
          f'\nTempo para fechar a aba do WhatsApp Web: ' + Fore.RED + Style.DIM + f'{tempo_fechar}')

time.sleep(5)
while len(contatos) >= 1 and cont < 3:
    os.system('cls') or None
    print(f'{title_msg} em operação. Aguarde {tempo} segundos...')
    # n.show_toast(title_msg, f"Enviando a mensagem para o contato {contatos[0]}, aguarde...\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!", duration=time_msg, icon_path=icon)
    try:
        if tipo_msg == 'imagem':
            pywhatkit.sendwhats_image(contatos[0], imagem, msg, tempo, fechar, tempo_fechar)
        if tipo_msg == 'texto':
            if contatos[0].startswith('+'):
                print(f'{contatos[0]} é número')
                pywhatkit.sendwhatmsg(contatos[0], msg, datetime.now().hour, datetime.now().minute + (tempo / 100))
            elif contatos[0].isascii():
                print(f'{contatos[0]} é ascii')
                pywhatkit.sendwhatmsg_to_group(contatos[0], msg, datetime.now().hour, datetime.now().minute + (tempo / 100))

        del contatos[0]
        # print(f'Mensagem enviada para o contato {contatos[0]}.\nContato restante: {len(contatos)}.\n{contatos}\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!')
        if len(contatos) <= 1:
            # n.show_toast(title_msg, f'Mensagem enviada para o contato {contatos[0]}.\nContato restante: {len(contatos)}.\n{contatos}\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!', duration=time_msg, icon_path=icon)
            print(f'Mensagem enviada para o contato {contatos[0]}.\nContato restante: {len(contatos)}.\n{contatos}\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!')
        if len(contatos) > 1:
            # n.show_toast(title_msg, f'Mensagem enviada para o contato {contatos[0]}.\nContatos restantes: {len(contatos)}.\n{contatos}\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!', duration=time_msg, icon_path=icon)
            print(f'Mensagem enviada para o contato {contatos[0]}.\nContatos restantes: {len(contatos)}.\n{contatos}\nFAVOR NÃO MEXER NO MOUSE DURANTE TODO O PROCESSO!')
    except:
        print(f'Falha ao enviar para o contato {contatos[0]}. Tentando novamente...')
        # n.show_toast(title_msg, f'Falha ao enviar para o contato {contatos[0]}.\nTentando novamente...', duration=time_msg, icon_path=icon)
        keyboard.press_and_release('ctrl + w')
        print(f'Aba do WhatsApp fechada...')
        cont+=1

    print(f'Contatos restantes: {len(contatos)}\n{contatos}')

print('Fim dos envios!')
# n.show_toast(title_msg, 'Fim da operação do WhatsBOT. Obrigado por utilizar!', duration=10, icon_path=icon)
time.sleep(10)
exit()
