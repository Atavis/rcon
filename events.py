import berconpy as rcon

async def on_message(message: str):
    """
        Отлавливает любое сообщение от сервера
        message - сообщение
    """
    print(f'[SERVER] {message}')

async def on_player_connect(player: rcon.Player):
    """
        Срабатывает когда игрок подсоединяется к серверу
        player - игрок

        print(f'[on_player_connect] {player.id}')
        print(f'[on_player_connect] {player.name}')
        print(f'[on_player_connect] {player.guid}') Не выводит на этой стадии
        print(f'[on_player_connect] {player.addr}')
        print(f'[on_player_connect] {player.ping}') Не выводит на этой стадии
        print(f'[on_player_connect] {player.is_guid_valid}')
        print(f'[on_player_connect] {player.in_lobby}')
        print(f'[on_player_connect] {player.cache}')
        print(f'[on_player_connect] {player.client}')
        print(f'[on_player_connect] {player.ip}')
    """
    print(f'[on_player_connect] {player}')




async def on_player_disconnect(player: rcon.Player):
    """
        Срабатывает когда игрок отсоединяется от сервера
        player - игрок

        print(f'[on_player_disconnect] {player.id}')
        print(f'[on_player_disconnect] {player.name}')
        print(f'[on_player_disconnect] {player.guid}')
        print(f'[on_player_disconnect] {player.addr}')
        print(f'[on_player_disconnect] {player.ping}')
        print(f'[on_player_disconnect] {player.is_guid_valid}')
        print(f'[on_player_disconnect] {player.in_lobby}')
        print(f'[on_player_disconnect] {player.cache}')
        print(f'[on_player_disconnect] {player.client}')
        print(f'[on_player_disconnect] {player.ip}')
    """
    print(f'[on_player_disconnect] {player}')


async def on_player_guid(player: rcon.Player):
    """
        Срабатывает когда сервер получает GUID игрока
        player - игрок

        print(f'[on_player_guid] {player.id}')
        print(f'[on_player_guid] {player.name}')
        print(f'[on_player_guid] {player.guid}')
        print(f'[on_player_guid] {player.addr}')
        print(f'[on_player_guid] {player.ping}') Не выводит на этой стадии
        print(f'[on_player_guid] {player.is_guid_valid}')
        print(f'[on_player_guid] {player.in_lobby}')
        print(f'[on_player_guid] {player.cache}')
        print(f'[on_player_guid] {player.client}')
        print(f'[on_player_guid] {player.ip}')
    """
    print(f'[on_player_guid] {player}')


async def on_player_kick(player: rcon.Player, reason: str):
    """
        Срабатывает когда игрока кикают сервера
        player - игрок
        reason - причина
    """
    print(f'[on_player_kick] {player} {reason}')

async def on_player_verify_guid(player: rcon.Player):
    """
        Срабатывает когда сервер проверяет GUID игрока
        player - игрок

        print(f'[on_player_verify_guid] {player.id}')
        print(f'[on_player_verify_guid] {player.name}')
        print(f'[on_player_verify_guid] {player.guid}')
        print(f'[on_player_verify_guid] {player.addr}')
        print(f'[on_player_verify_guid] {player.ping}') Не выводит на этой стадии
        print(f'[on_player_verify_guid] {player.is_guid_valid}')
        print(f'[on_player_verify_guid] {player.in_lobby}')
        print(f'[on_player_verify_guid] {player.cache}')
        print(f'[on_player_verify_guid] {player.client}')
        print(f'[on_player_verify_guid] {player.ip}')
    """
    print(f'[on_player_verify_guid] {player}')


async def on_raw_event(packet):
    """
        Срабатывает для каждого анализируемого пакета
        packet - пакет
    """
    print(packet)

async def on_login():
    """
        Срабатывает когда RCON подключается к серверу
    """
    print("Подключение к RCON")