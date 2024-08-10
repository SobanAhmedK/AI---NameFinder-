import csv


def read_prompt(file_path):
    """Reads the prompt written in the file."""
    with open(file_path, "r") as file:
        return file.read().strip()


def store_response_in_csv(list_of_response, csv_filepath="output.csv"):
    """Stores the list of responses in a CSV file."""
    file_exists = False
    try:
        file_exists = open(csv_filepath).readline()
    except FileNotFoundError:
        pass

    with open(csv_filepath, "a", newline="") as csvfile:
        fieldnames = ["name", "availability", "price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file is empty
        if not file_exists:
            writer.writeheader()

        writer.writerows(list_of_response)
