import time
from helper_functions.domain_checker import name_checker
from helper_functions.namefinder import name_finder
from helper_functions.utils import read_prompt, store_response_in_csv


def main():
    prompt_filepath = "helper_functions/prompt.txt"
    prompt = read_prompt(prompt_filepath)

    for _ in range(20):
        names = name_finder(prompt)
        print(names)
        name_checker_response = name_checker(names)
        print(name_checker)
        store_response_in_csv(name_checker_response)
        time.sleep(5)


if __name__ == "__main__":
    main()
