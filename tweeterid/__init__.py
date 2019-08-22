import requests
import json


def handle_to_id(handle: str) -> int:
    Id = requests.post(
        'https://tweeterid.com/ajax.php',
        data={
            'input': handle
        }
    ).content.decode()
    return int(Id)


def id_to_handle(id_: int) -> str:
    handle = requests.post(
        'https://tweeterid.com/ajax.php',
        data={
            'input': str(id_)
        }
    ).content.decode()
    return handle
