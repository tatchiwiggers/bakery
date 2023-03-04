from typing import List


class __ClientRepository:
    def __init__(self) -> None:
        self.__client_list = []

    def insert_client(self, client: any) -> None:
        self.__client_list.append(client)

    def return_all_clients(self) -> List:
        return self.__client_list


client_repository = __ClientRepository()

