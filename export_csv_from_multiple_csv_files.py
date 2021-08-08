import sys
import pandas as pd
import os

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

if __name__ == '__main__':
    # Install pandas if you do not have already
    os.system("pip install pandas")
    
    # str(sys.argv[1]) is the path we want to save our combined csv file and sys.argv[2:] the paths of the csv files we want to combine
    Create_the_combined_csv_file(str(sys.argv[1]),sys.argv[2:])