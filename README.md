# PythonExamples

## export_csv_from_multiple_csv_files.py

## Concatenate rows of multiple CSV files to one CSV file
To create a combined csv file from multiple csv files run in your command line:

python export_csv_from_multiple_csv_files.py concatenate {name of the csv file to create} {csv file 1} {csv file 2} {csv file 3} etc.

### Example

python export_csv_from_multiple_csv_files.py concatenate C:/Users/DataViz/Combined_Stats.csv C:/Users/DataViz/Births.csv C:/Users/DataViz/Deaths.csv C:/Users/DataViz/Population.csv

## Join CSV files

To join two or multiple CSV files run in your command line:

python export_csv_from_multiple_csv_files.py merge {name of the csv file to create} {column} {type of join (left, right, outer, inner, cross)} {csv file 1} {csv file 2} {csv file 3} etc.

python export_csv_from_multiple_csv_files.py merge C:/Users/DataViz/Combined_Stats.csv country_id left C:/Users/DataViz/Births.csv C:/Users/DataViz/Deaths.csv C:/Users/DataViz/Population.csv