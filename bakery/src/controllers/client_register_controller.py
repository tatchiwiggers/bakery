from typing import Dict
from src.models.models import Client
from src.models.repositories.clients_repository import client_repository


class ClientRegisterController:
    def insert(self, new_client_information: Dict) -> Dict:
        try:
            client = self.__create_client_entity(new_client_information)
            self.__registry_client(client)
            response = self.__format_response(new_client_information)
            return response
        except KeyError:
            return { "success": False, "error": "Error in insert client" }

    def __create_client_entity(self, new_client_information: Dict):
        name = new_client_information['name']
        phone = new_client_information['phone']
        state = new_client_information['state']
        
        client = Client(name, phone, state)
        return client

    def __registry_client(self, client: any):
        client_repository.insert_client(client)

    def __format_response(self, new_client_information: Dict) -> Dict:
        return {
            "success": True,
            "attributes": {
                "registry": 1,
                "name": new_client_information["name"],
                "phone": new_client_information["phone"],
                "state": new_client_information["state"],
            },
        }

client_register_controller = ClientRegisterController()