import sys
import pandas as pd
import os

def Run(action, *args):
    if action == 'merge':
        Merge(args)
    elif action == 'concatenate':
        Create_the_combined_csv_file(args)

def Create_the_combined_csv_file(export_filename, *args):

    # CSV to Pandas DataFrame the first 2 CSV files
    csv_1 = pd.read_csv(f'{args[0][0]}')
    csv_2 = pd.read_csv(f'{args[0][1]}')

    # Append the first csv to the other
    export_csv = csv_1.append(csv_2, ignore_index=True)

    # If more than 2 CSV files have been mentioned in command line this will run
    try:
        # For every extra csv file we are creating a Pandas DataFrame and then append it to the existing one to export
        for arg in args[0][2:]:
            csv_2 = pd.read_csv(f'{arg}')
            export_csv = export_csv.append(csv_2, ignore_index=True)
    except:
        pass

    # After appending all the Pandas DataFrame to the export_csv DataFrame we are exporting it to a CSV file with the name mentioned in the command line
    export_csv.to_csv(f'{export_filename}', index=False)

def Merge(export_filename, column, join, *args):

    # CSV to Pandas DataFrame the first 2 CSV files
    csv_1 = pd.read_csv(f'{args[0][0]}')
    csv_2 = pd.read_csv(f'{args[0][1]}')

    # Append the first csv to the other
    export_csv = csv_1.merge(csv_2, on=column, how=join)

    # If more than 2 CSV files have been mentioned in command line this will run
    try:
        # For every extra csv file we are creating a Pandas DataFrame and then append it to the existing one to export
        for arg in args[0][2:]:
            csv_2 = pd.read_csv(f'{arg}')
            export_csv = export_csv.merge(csv_2, on=column, how=join)
    except:
        pass

    # After appending all the Pandas DataFrame to the export_csv DataFrame we are exporting it to a CSV file with the name mentioned in the command line
    export_csv.to_csv(f'{export_filename}', index=False)

if __name__ == '__main__':
    # Install pandas if you do not have already
    os.system("pip install pandas")

    try:
        Run(str(sys.argv[1]),str(sys.argv[2]),sys.argv[3:])
    except:
        print('You should state more arguments')