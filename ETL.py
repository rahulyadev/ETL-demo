import camelot
print("start")

table_areas = ["37.5,719,206.69,84"]
columns = ["49.8", "57.68", "61.7"]
# Extract tables from PDF
tables = camelot.read_pdf("/Users/parry/Downloads/Test_PDF.pdf", pages='all', flavor='stream', table_areas=table_areas, columns=columns)


# Accessing the tables
for i, table in enumerate(tables):
    df = table.df  # Convert to DataFrame
    print(f"Table {i} Preview:")
    print(df)  # Inspect the first few rows

    # Optional: Save to CSV
    df.to_csv(f'table_{i}.csv', index=False)