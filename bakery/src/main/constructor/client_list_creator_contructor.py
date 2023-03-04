from src.views.client_register_view import ClientRegisterViews
from src.controllers.client_list_creator_controller import ClientListCreator
from src.views.client_list_view import ClientListViews


def client_list_creator_process():
    client_register_view = ClientRegisterViews()
    client_list_controller = ClientListCreator()
    client_list_view = ClientListViews()


    response = client_list_controller.create_client_list()

    client_register_view.registry_client_view()

    if response["success"]: client_register_view.registry_client_success(response["playlist"])
    else: client_register_view.registry_client_success(response["error"])