""" S10Q01
INVENTORY REPORT PROBLEM:
Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter.

"""
import sys
import invcost as k
import csv

def read_inventory(filename):
    try:
        inventory = list()
        i = 0
        with open(filename) as FH:
            rows = csv.reader(FH)
            headers = next(rows)
            for row in rows:
                inventory.append((row[0],int(row[1]),float(row[2])))
            i += 1
    except FileNotFoundError:
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return inventory
            
            
            
# Main starts here
if __name__ == "__main__":
#    inventory = list()
    inventory = read_inventory("Data\inventory.csv")
    print(inventory)
    inv_cost = sum(p[1]*p[2] for p in inventory)
    print("inv_cost:",inv_cost)
        
        
        


