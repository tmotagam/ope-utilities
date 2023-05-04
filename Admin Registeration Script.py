# OPE Utilities
# Copyright (C) 2023 Motagamwala Taha Arif Ali

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see
# <https: //www.gnu.org/licenses />.
from requests import get, post
from termcolor import colored
from webbrowser import open


def registeradmin(url):
    try:
        name = input(
            colored(
                "Please enter your name: \t",
                "yellow",
            )
        )
        email = input(
            colored(
                "Please enter your communication Id eg. (example@exampleemail.org): \t",
                "yellow",
            )
        )
        while True:
            password = input(
                colored(
                    "Please enter your password: \t",
                    "yellow",
                )
            )
            confirmedpassword = input(
                colored(
                    "Please confirm your password: \t",
                    "yellow",
                )
            )
            if password != confirmedpassword:
                print(
                    colored(
                        "Enter your password correctly",
                        "red",
                    )
                )
                continue
            else:
                break
        res = post(
            url,
            json={
                "comType": "EMAIL",
                "comid": email,
                "name": name,
                "type": "ADMIN",
                "password": password,
                "confirmPassword": confirmedpassword,
            },
        )
        if res.status_code == 200:
            c = res.json()
            print(colored(c["message"], "green"))
            return c["id"]
        else:
            c = res.json()
            print(colored(c["error"], "red"))
            return ""
    except:
        print(colored("Error occurred \n", "red"))
        return ""


def verifyadmin(url):
    try:
        code = input(
            colored(
                "Please enter your OTP: \t",
                "yellow",
            )
        )
        payload = f'--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name="code"\r\n\r\n{code}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n'
        res = post(
            url=url,
            data=payload,
            headers={
                "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A"
            },
        )

        if res.status_code == 200:
            c = res.json()
            print(colored(c["message"], "green"))
            return "success"
        else:
            c = res.json()
            print(colored(c["error"], "red"))
            return "error"

    except:
        print(colored("Error occurred \n", "red"))
        return "error"


def check_server_url(url):
    try:
        res = get(url + "#/")
        if res.status_code == 200:
            print(colored("Server is active \n", "green"))
            print(colored("Moving on to admin registration phase \n", "green"))
            uid = registeradmin(url + "auth/register")
            if uid == "":
                return
            else:
                print(colored("Moving on to admin verification phase \n", "green"))
                r = verifyadmin(url + f"auth/userverification/{uid}/ADMIN")
                if r == "success":
                    print(
                        colored(
                            "Admin is now created successfully use the userid given below to login into the system \n",
                            "green",
                        )
                    )
                    print(colored(f"userid: {uid} \n", "green"))
                    open(url + "#/", autoraise=True)
                else:
                    return
        else:
            print(
                colored(
                    "Make sure server is active before executing this script \n", "red"
                )
            )
    except:
        print(
            colored("Make sure server is active before executing this script \n", "red")
        )


print(colored("Admin Registeration and Verification Script for OPE \n", "green"))
check_server_url(
    input(colored("Enter the Server URL eg. (http(s)://127.0.0.1:3000/): \t", "yellow"))
)
