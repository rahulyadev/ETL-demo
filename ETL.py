print("start")
import camelot

# Extract tables from PDF
tables = camelot.read_pdf("/Users/parry/Downloads/Test_PDF.pdf", pages='all', flavor='stream')


# Accessing the tables
for i, table in enumerate(tables):
    df = table.df  # Convert to DataFrame
    print(f"Table {i} Preview:")
    print(df.head())  # Inspect the first few rows

    # Optional: Save to CSV
    # df.to_csv(f'table_{i}.csv', index=False)