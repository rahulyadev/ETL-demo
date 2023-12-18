import camelot
import matplotlib.pyplot as plt

# Load the PDF
file_path = '/Users/parry/Downloads/Test_PDF.pdf'
tables = camelot.read_pdf(file_path, flavor='stream', pages='1')

# Plot the grid
plot = camelot.plot(tables[0], kind='grid')
plt.show()