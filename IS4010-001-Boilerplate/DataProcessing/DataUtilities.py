
import csv

def read_customer_dataset():
    file_path = "Data/Customer.csv"  # Adjust path if needed

    # Open the file with UTF-16 encoding and read it properly
    with open(file_path, mode="r", encoding="utf-16", errors="replace") as infile:
        reader = csv.DictReader(infile, delimiter="\t")  # Tab-separated format
        return [row for row in reader]  # Convert to a list of dictionaries