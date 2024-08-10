"""This file will be responsible for checking the name availability on the Godaddy

Inputs: Array of Names
functionality: Send the names to goDaddy.com one by one and see the status of names given
Output: return list of responses




"""


def name_checker(names: list):
    list_of_response = [
        {
            "name": "Name of domain",
            "availbility": "Availability of domain",
            "price": "price of domain",
        }
    ]
    return list_of_response
