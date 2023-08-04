# This line imports the operating system into the file.
import os

# This line imports "Path" from the "pathlib" module.
from pathlib import Path

# This line imports "csv" module and allows us to use the data from the csv files into this file. 
import csv

# This line of code calls "os.getcwd()" and assigns the returned path to the variable "original_working_dir".
original_working_dir = os.getcwd()

# This lines sets the current working directory to the folder containing the CSV file. 
csv_folder = os.path.join(os.getcwd(), "csv_reports")
os.chdir(csv_folder)

# This line opens and reads the CSV file.
csv_file = "Overheads.csv"

# This opens and reads the csv file.
with open(csv_file, mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

# This skips the header row as it contains column names that are not needed. 
    next(reader)

# This assigns an empty list to the variable overhead_data. 
    overhead_data = []

# This is a loop that will execute the code for each row of data in reader. 
    for row in reader:

# This appends the list for the code and creates a new list with converted upper case words and float value
        overhead_data.append([row[0].upper(), float(row[1])])

# This helps defines the function "find_highest_overhead" with the parameter "data".
def find_highest_overhead(data):

# This line initialises the variable.
    highest_overhead = data[0]

# This is a loop that will execute the code for each row of data in overhead. 
    for overhead in data:

# This "if" function checks if the second element of the current "overhead" is greater than the second element of the "highest_overhead". 
# If the condition is true, the current element has a higher value in the second element that the previously store "highest_overhead".
        if overhead[1] > highest_overhead[1]:

# This line carries out the "if" function if its "True" and the "highest_overhead" is updated to the current "overhead".
            highest_overhead = overhead

# This line returns the element that had the highest value in the data.
    return highest_overhead

# This line changes the directory from the operating system back to the original.
os.chdir(original_working_dir)
