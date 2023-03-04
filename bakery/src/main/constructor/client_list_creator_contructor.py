from src.controllers.client_list_creator_controller import ClientListCreator
from src.views.client_register_view import ClientRegisterViews


def client_list_creator_process():
    client_list_view = ClientRegisterViews()
    client_list_controller = ClientListCreator()

    client_list_view.registry_client_view()
    response = client_list_controller.create_client_list()

    if response["success"]: client_list_view.registry_client_success(response["playlist"])
    else: client_list_view.registry_client_success(response["error"])