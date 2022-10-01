import subprocess

import requests
from colorama import Back, init as colorama_init
from requests.exceptions import ConnectTimeout, ConnectionError, HTTPError, \
    ReadTimeout


def main():
    colorama_init(autoreset=True)

    try:
        status_code = requests.get(
            "https://github.com/moayad-star/IP-info").status_code
        if status_code == 404:
            print(
                Back.RED
                + "Sorry, the project does not exist\nIt may have been deleted :("
            )
            exit(1)

        if status_code != 200:
            raise HTTPError(
                f"Unexpected response code: {status_code}")

        print(Back.GREEN + "Connection status: good")
    except (
            ConnectTimeout,
            ConnectionError,
            ReadTimeout,
    ):
        print(Back.RED + "You are offline!")
        exit(1)
    except HTTPError as e:
        print(Back.RED + str(e))
        exit(1)

    print("\nUpdating the repo...")
    subprocess.run(["git", "pull"])
    print(Back.GREEN + "Updated successfully!")


main()
