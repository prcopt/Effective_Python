import csv
import sys
import pathlib

def inventory_cost(filename):
    try:
        with open(filename) as FH:
            rows = csv.reader(FH)
            print("Rows:",rows)
            headers = next(rows)
            total = 0.0
            for row_no, row in enumerate(rows,start=1):
                try:
                    quant = int(row[1])
                    price = float(row[2])
                    total += quant*price
                except ValueError as e:
                    print("Row:",row_no,"Bad row",row)
                    print("Reason",e)
    except FileNotFoundError:
        print("File:",filename[filename.rfind("\\")+1:]," Not Found: Execution Terminated")
        sys.exit("")
    return total

def test():
    print ("TEST")
    

def get_folder_path_and_filename(fname):
    path = str(pathlib.Path(__file__).parent.resolve())+'\\Data\\'
    return path+fname

#Main Starts here
# Main starts here
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = get_folder_path_and_filename(sys.argv[1])
    else:
        fname = str.upper(input("Enter Inventory File Name:"))
        filename = get_folder_path_and_filename(fname)

    cost = inventory_cost(filename)
    print("Total Cost",cost)

