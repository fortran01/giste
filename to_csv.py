"""
This script converts all SAS dataset files (.sas7bdat) in the current directory to CSV format.
It automatically:
1. Finds all .sas7bdat files in the current directory
2. Reads each SAS file using pandas
3. Cleans any binary strings by converting them to UTF-8 text
4. Saves each dataset as a CSV file with the same base filename
"""

import os
import pandas as pd

# Find all .sas7bdat files in current directory
sas_files = [f for f in os.listdir('.') if f.endswith('.sas7bdat')]

# Convert each file to CSV
for sas_file in sas_files:
    # Read SAS file
    df = pd.read_sas(sas_file)

    # Clean binary strings from all object (string) columns
    object_columns = df.select_dtypes(include=['object']).columns
    for col in object_columns:
        # Convert bytes to strings if column contains bytes objects
        if df[col].dtype == 'object' and isinstance(df[col].iloc[0], bytes):
            df[col] = df[col].str.decode('utf-8')

    # Create CSV filename by replacing extension
    csv_file = os.path.splitext(sas_file)[0] + '.csv'

    # Save as CSV
    df.to_csv(csv_file, index=False)
    print(f"Converted {sas_file} to {csv_file}")
