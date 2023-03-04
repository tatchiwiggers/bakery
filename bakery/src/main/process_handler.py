from src.main.constructor.introduction_process import introduction_process
from src.main.constructor.client_register_constructor import client_register_proccess
from src.views.client_list_view import ClientListViews
from src.controllers.client_list_creator_controller import ClientListCreator

def start():
    while True:
        command = introduction_process()
        if command == '1':
            client_register_proccess()
        elif command == '2':
                clients = ClientListCreator().get_all_clients()
                ClientListViews().client_list_view(clients)
        elif command == '6':
            exit()
        else:
            print('Error')
