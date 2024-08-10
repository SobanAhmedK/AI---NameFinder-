import time
from domain_checker import name_checker
from namefinder import name_finder
from utils import read_prompt, store_response_in_csv


def main():
    prompt_filepath = "prompt.txt"
    prompt = read_prompt(prompt_filepath)

    for _ in range(20):
        names = name_finder(prompt)
        name_checker_response = name_checker(names)
        store_response_in_csv(name_checker_response)
        time.sleep(5)


if __name__ == "__main__":
    main()
