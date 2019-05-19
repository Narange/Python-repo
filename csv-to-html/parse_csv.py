# Parse through the records in the CSV file and output to an HTML list

import csv
import os.path

html_output = ""
names = []

with open("patrons.csv", "r") as data_file:
    csv_data = csv.reader(data_file)

    # skip first two lines (headers and a line of example data)
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == "No Reward":
            break
        names.append(f"{line[0]} {line[1]}")

html_output += f"<p>There are {len(names)} people in this list.</p>"

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += "\n</ul>"

# check if result.html exists before we create it
result_file_exists = os.path.isfile("result.html")

# write the resulting list in a new HTML file
with open("result.html", "w") as wf:
    wf.write(html_output)

if result_file_exists:
    print("result.html already existed, and was overwritten")
else:
    print("result.html has been created")
