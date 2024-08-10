from domain_checker import name_checker
from namefinder import name_finder


def read_prompt(file_path):
    """read_prompt Reading the prompt written in file

    :param _type_ file_path: path of file
    """
    with open(file_path, "r") as file:
        return file.read()


prompt_filepath = "prompt.txt"
prompt = read_prompt(prompt_filepath)

names = name_finder(prompt)
name_checker_response = name_finder(names)

