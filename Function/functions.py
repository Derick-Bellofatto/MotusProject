import os
import csv
import re

def read_customer_dataset():
    """Reads and cleans the customer dataset from a UTF-16 tab-separated CSV file."""
    file_path = "Data/Customer.csv"  # Path to the customer dataset

    with open(file_path, mode="r", encoding="utf-16", errors="replace") as infile:
        reader = csv.DictReader(infile, delimiter="\t")  # Read as tab-separated values
        data = list(reader)  # Convert to a list of dictionaries
        return data

def sanitize_filename(name):
    """Sanitizes filenames by replacing or removing problematic characters."""
    name = name.strip()
    name = name.replace(" ", "_").replace("&", "and")  # Standard replacements
    name = re.sub(r'[\/:*?"<>|]', '_', name)  # Replace forbidden characters with "_"
    return name

def export_customer_data():
    """Processes the customer dataset, groups by customer, and exports to individual CSV files."""
    customer_records = read_customer_dataset()  # Read and clean data

    if not customer_records:
        print("No customer records found.")
        return

    customer_groups = {}  # Dictionary to store grouped customer data

    # Group data by customer name
    for record in customer_records:
        customer_name = record.get("Customer", "").strip()

        if not customer_name:
            print("Skipping record with missing Customer field:", record)
            continue  # Skip records without a valid customer name
        
        if customer_name not in customer_groups:
            customer_groups[customer_name] = []
        
        customer_groups[customer_name].append(record)

    # Define output directory inside 'DataExport'
    output_dir = "DataExport"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

    # Write each customer's data to a separate CSV file
    for customer_name, records in customer_groups.items():
        sanitized_name = sanitize_filename(customer_name)  # Sanitize filename
        file_path = os.path.join(output_dir, f"{sanitized_name}.csv")

        if not records:
            print(f"Skipping empty customer file for: {customer_name}")
            continue  # Skip writing empty files

        # Open the file and write customer data
        with open(file_path, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=records[0].keys())
            writer.writeheader()  # Write column headers
            writer.writerows(records)  # Write customer data

        print(f"✅ Exported: {file_path} ({len(records)} records)")

        print(f"Checking if folder exists: {os.path.exists(output_dir)}")
        print(f"Writing file: {file_path} with {len(records)} records")



