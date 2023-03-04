from src.controllers.client_register_controller import ClientRegisterController
from src.views.client_register_view import ClientRegisterViews


def client_register_proccess():
    client_register_view = ClientRegisterViews()
    client_register_controller = ClientRegisterController()

    new_client_informaions = client_register_view.registry_client_view()
    response = client_register_controller.insert(new_client_informaions)

    if response['success']:
        client_register_view.registry_client_success(response['attributes'])
    else:
        client_register_view.registry_client_fail(response['error'])
