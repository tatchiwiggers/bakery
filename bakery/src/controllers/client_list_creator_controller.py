from typing import Dict, List
from src.models.repositories.clients_repository import client_repository


class ClientListCreator:
    def create_client_list(self) -> Dict:
        try:
            client_list = self.__get_all_clients()
            return self.__format_response(client_list)
        except Exception as exception:
            return {'success': False, 'error': str(exception)}

    def __get_all_clients(self) -> List:
        clients = client_repository.return_all_clients()
        if clients is []: raise Exception('No registred clients')
        return clients

    def __format_response(self, client_list: List) -> Dict:
        return {
            'success': True,
            'client_list': client_list
        }


client_list_creator = ClientListCreator()

