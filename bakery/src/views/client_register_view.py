import os
from typing import Dict


class ClientRegisterViews:
    def registry_client_view(self) -> str:
        self.__clear()

        print('Insert new client \n\n')
        name = input('Type the client name: ')
        phone = input('Type the client phone: ')
        state = input('Type the client state: ')

        new_client_informations = {
            'name': name, 'phone': phone, 'state': state
        }
        return new_client_informations

    def registry_client_success(self, client_registry: Dict) -> None:
        self.__clear()

        message = '''
            Client registred
            * Infos:
                Client Name: {}
                Client Phone: {}
                Client State: {}
        '''.format(
            client_registry['name'],
            client_registry['phone'],
            client_registry['state']
        )
        print(message)

    def registry_client_fail(self, error: str) -> None:
        self.__clear()

        message = f'''
            Error inserting client
            {error}
        '''
        print(message)

    def __clear(self):
        os.system('cls || clear')
