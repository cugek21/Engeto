data_1 = {
    'order': {
        'id': '1234', 'type': 'order.created', 'channel': 'eshop CZ'
    }
}

data_2 = {
    'order': {
        'id': '1234', 'type': 'order.created', 'channel': ''
    }
}

data_3 = {
    'order': {
        'id': '1234', 'type': 'order.created'
    }
}

vlozeny_dict = dict[str, dict[str, str]]

def vrat_objednavky(data: vlozeny_dict) -> str:
    try:
        return data['order']['channel'].split(' ')[-1]

    except KeyError:
        return 'No channel found.'
    except IndexError:
        return 'Channel is empty.'

print(vrat_objednavky(data_3))