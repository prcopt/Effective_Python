""" When inventory files have the flexibility to order the data in random columns
    The earlier version checked-in will also work with inventorydate.csv where an
    additional Date information is also provided.
"""
import csv
import sys
import pathlib

def inventory_cost(filename):
    try:
        with open(filename) as FH:
            rows = csv.reader(FH)
            header = next(rows)
            total = 0
            for row_no, row in enumerate(rows,start=1):
                try:
                    values = row
                    set = dict(zip(header,values))
                    total += float(set['price'])*int(set['quant'])
                except ValueError as e:
                    print("ValueError: Row:",row_no,"Couldn't convert:",row)
                    print("Reason:",e)
                except IndexError as e:
                    print("IndexError: Row:",row_no,"Skipping a row:",row)
                    print("Reason:",e)
                    continue
                except KeyError as e:
                    print("KeyError: Row:",row_no,"Skipping a row:",row)
                    print("Reason:",e)
            
    except FileNotFoundError:
        print("File:",filename[filename.rfind("\\")+1:]," Not Found: Execution Terminated")
        sys.exit("")
    return total


    

def get_folder_path_and_filename(fname):
    path = str(pathlib.Path(__file__).parent.resolve())+'\\Data\\'
    return path+fname

#Main Starts here
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = get_folder_path_and_filename(sys.argv[1])
    else:
        fname = str.upper(input("Enter Inventory File Name:"))
        filename = get_folder_path_and_filename(fname)

    cost = inventory_cost(filename)
    print("Total Cost",cost)

