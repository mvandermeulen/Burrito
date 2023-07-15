import socket

import requests
from dotenv import dotenv_values, find_dotenv
import rich


__env_path = find_dotenv()
__port_data = []
__base_url = "http://localhost:{}/docs"

print("Test version \n\n")

if __env_path:
    rich.print(f"[green][+] Found .env file: {__env_path}")
    __config = dotenv_values(__env_path)

    for key, value in __config.items():
        if key.startswith("BURRITO_PORT_"):
            __port_data.append((key, value))
            rich.print(f"\t[blue]Option {key} => {value}")


def _ping(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(("localhost", int(data[1])))
        rich.print(f"\t[green][+] Host is OK: {data}")
    except:
        rich.print(f"\t[red][-] No connection to host: {data}")
    finally:
        sock.close()


# check host availability
rich.print("\n[blue][*] Checking for host accessability")
for host in __port_data:
    _ping(host)


# get host docs
rich.print("\n[blue][*] Checking for docs accessability")
for host in __port_data:
    url = __base_url.format(host[1])

    try:
        response = requests.get(url)
        rich.print(f"\t[green][+] Docs is available for host: {host} via url {url}")
    except:
        rich.print(f"\t[red][-] Docs is not available for host: {host} via url {url}")