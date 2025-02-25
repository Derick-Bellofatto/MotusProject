# main.py
# IS4010-001 Boilerplate Project

import os

from DataProcessing.DataUtilities import *
from Function.functions import export_customer_data

if __name__ == "__main__":
    export_customer_data()


    
    """
    #print("Column Names:", customer_records[0].keys())  # Print the keys of the first dictionary

    customer_groups = {}
    for record in customer_records:
        # Extract the customer name from the record.
        # The `.get('Customer', '')` method ensures that if 'Customer' is missing, it returns an empty string instead of an error.
        # `.strip()` removes any leading or trailing spaces from the name.
        customer_name = record.get('Customer', '').strip()  

        # If the customer_name is empty (meaning the field was missing or blank), print a message and skip this record.
        if not customer_name:
            print("Skipping record due to missing Customer field:", record)
            continue  # Move to the next record in the loop

        # If this is the first time encountering this customer, add an empty list in the dictionary for them.
        if customer_name not in customer_groups:
            customer_groups[customer_name] = []  # Create an empty list for this customer.

        # Add the current record to the customer's list in the dictionary.
        customer_groups[customer_name].append(record)

    for customer_name, records in customer_groups.items():
        print(f"\nCustomer: {customer_name} ({len(records)} records)")  # Print the customer name and how many records they have

        # Print only the first 3 records for each customer to avoid excessive output.
        for record in records[:3]:  
            print(record)  # Print the record (which is a dictionary representing a row from the CSV file)
            


    # Initialize an empty dictionary to store customer groups.
    # Initialize an empty dictionary to store customer groups.
    customer_groups = {}

    # Loop through each record in customer_records
    for record in customer_records:
        customer_name = record.get('Customer', '').strip()  # Get the customer name and remove extra spaces.


        if not customer_name:
            print("Skipping record due to missing Customer field:", record)  # Debugging
            continue  # Skip records with missing customer names.

        if customer_name not in customer_groups:
            customer_groups[customer_name] = []  # Create an empty list for this customer.

        customer_groups[customer_name].append(record)  # Add the record to the customer's list.

    output_dir = "Exported_Customers"
    os.makedirs(output_dir, exist_ok=True)

    for customer_name, records in customer_groups.items():
        sanitized_name = customer_name.replace(" ", "_").replace("&", "and").replace(",", "").replace(".", "")
        file_path = os.path.join(output_dir, f"{sanitized_name}.csv")

        with open(file_path, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=records[0].keys())
            writer.writeheader()  # Write column headers
            writer.writerows(records)  # Write customer data

        print(f"Exported: {file_path}")  # Confirmation message
    
        """


