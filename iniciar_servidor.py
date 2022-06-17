from os import system
from threading import Thread

try:
    def inicia():
        system("start python manage.py runserver > nul")


    def second_thread():
        system("start chrome.exe 127.0.0.1:8000")


except KeyboardInterrupt:
    system("cls && color A")
    print('-'*50)
    print("Programa finalizado com sucesso!")
    print('-'*50)
    print()
    print()
    print("  | ___________ |\n  | | - | |\n  | | | |\n  | |_________| |________________________\n  \=____________/ By Makalau)\n  / \"\"\"\"\"\"\"\"\"\"\"\\/\n / ::::::::::::: \ :D-'\n(_________________)")
    print()
    print()    
    system("pause")
 
obj_thread_1 = Thread(target=inicia)
obj_thread_2 = Thread(target=second_thread)

obj_thread_1.start()
obj_thread_2.start()
