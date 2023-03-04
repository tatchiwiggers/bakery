import os
from typing import List

class ClientListViews:
    def client_list_view(self, clients: List) -> None:
        print('Lista de CLientes: \n')

        for client in clients:
            message = '''
                Nome: {}
                Phone: {}
                State: {}

            '''.format(
                client.name,
                client.phone,
                client.state,
            )
            print(message)