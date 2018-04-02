import csv
import pandas as pd

'''
Program is a two parter. First part uses built-in CSV library to clean up the
downloaded CSV, by removing blank rows & only keeping the data we want to use.
It also appends heads to the top of our file.

The second part uses the Pandas library to import our CSV into a dataframe,
consolidate our results and then export back into the new CSV file.
'''


# List headers desired at top of CSV
headers = ['SKU',
           'DCP',
           'Description',
           'Sales Volume',
           'Available Stock'
           ]

# Open the downloaded CSV,and save the new CSV. Newline defined for windows.
with open("example_input.csv", "r") as inp, \
     open("example_output.csv", "w", newline="") as out:

    csvwriter = csv.writer(out)

    # Add headers to top of sheet
    csvwriter.writerow(headers)

    # Downloaded sheet is invalid CSV.
    # First step is to check for blank lines and skip them.
    for row in csv.reader(inp):
        if len(row) <= 2:
            pass
        else:
            # If the row isn't blank, check if the cell on the 3rd column is
            # blank. If it's not, then write the row to the new sheet.
            if row[2] != "":
                # Only write the following columns:
                csvwriter.writerow((row[0],
                                   row[1],
                                   row[2],
                                   row[4],
                                   row[11]))

# Load the newly created CSV into a Pandas dataframe.
df = pd.read_csv("example_output.csv")
# Check for any remaining blank rows and drop them from the dataframe.
df = df.dropna()
# Consolidate the dataframe values (like a one dimensional Pivot Table).
df = df.groupby(['SKU', 'DCP', 'Description']).sum()
# Write the now consildated date back to the new CSV file.
df.to_csv('example_output.csv')
