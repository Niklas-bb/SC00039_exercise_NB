import csv

# Step 1: Load the CSV file into a list of dictionaries
with open('brca_cnvs_tcga-1-2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)


# Step 2: Calculate the length of each segment (loc_end - loc_start)
for row in rows:
    loc_start = int(row['loc.start'])  # Convert string to integer
    loc_end = int(row['loc.end'])      # Convert string to integer
    row['segment_length'] = loc_end - loc_start

# Step 3: Save the updated data with the new column to a new CSV file
with open('brca_cnvs_tcga-1-2_updatedfile.csv', 'w', newline='') as csvfile:
    fieldnames = reader.fieldnames + ['segment_length']  # Add new column header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("New CSV file with segment lengths has been created.")

# Step 4: Read the new file and print it
with open('brca_cnvs_tcga-1-2_updatedfile.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)