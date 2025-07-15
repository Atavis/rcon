import asyncio
import math

from berconpy import AsyncRCONClient, AsyncRCONClientCache, AsyncEventDispatcher, AsyncClientConnector
from events import on_message, on_player_connect, on_player_disconnect, on_player_guid, on_player_kick, on_player_verify_guid, on_login

async def main():
    ip = "80.242.59.185"
    port = 2310
    password = "34sDk35khsku345"

    client = AsyncRCONClient(
        cache=AsyncRCONClientCache(),
        dispatch=AsyncEventDispatcher(),
        protocol=AsyncClientConnector()
    )

    client.add_listener("on_player_connect", on_player_connect)
    client.add_listener("on_player_disconnect", on_player_disconnect)
    client.add_listener("on_player_guid", on_player_guid)
    client.add_listener("on_message", on_message)
    client.add_listener("on_player_kick", on_player_kick)
    client.add_listener("on_player_verify_guid", on_player_verify_guid)
    client.add_listener("on_login", on_login)

    async with client.connect(ip, port, password):
        await asyncio.sleep(math.inf)

if __name__ == "__main__":
    asyncio.run(main())