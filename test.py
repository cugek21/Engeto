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

def vrat_objednavky(sheet: dict) -> None | str:
    try:
        channel = sheet['order']['channel']
        channel_split = channel.split()
        return channel_split[1]

    except KeyError:
        return 'No channel found.'
    except IndexError:
        return 'Channel is empty.'

print(vrat_objednavky(data_3))
