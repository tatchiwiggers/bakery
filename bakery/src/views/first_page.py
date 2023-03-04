def first_page():
    message = '''
    Bakery System

    * Register Client           [1]
    * Show all Clients          [2]
    * Show all Products         [3]
    * Show all Clients by State [4]
    * Delete Product            [5]
    * Exit                      [6]

    '''
    print(message)
    command = input('Option: ')
    
    return command
