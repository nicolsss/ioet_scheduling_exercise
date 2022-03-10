def get_start_color_msg(type_msg):
    """
    gets the color depending on the type of the message
    :param type_msg:
    :return:
    """
    return '\033[91m' if type_msg == 'error' else '\033[33m'


def print_msg(msg, type_msg):
    """
    Prints an orange message
    :param msg: str
        Text to be printed
    :param type_msg: str
        Type of message
    :return:
    """
    start_color = get_start_color_msg(type_msg)
    end_color = '\033[0m'
    print(start_color + msg + end_color)


def print_menu():
    """
    Prints menu options
    :return:
    """
    menu = """MENU
1. Calculate matching time frames employees'
2. Exit"""
    print(menu)
