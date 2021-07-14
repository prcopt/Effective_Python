"""  Read Inventory file modified from List of Tuples to List of Dictionaries

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
#            keys = headers.split()
            print(headers)
            for row in rows:
                inventory.append({headers[0]:row[0],headers[1]:int(row[1]),headers[2]:float(row[2])})
            i += 1
    except FileNotFoundError:
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return inventory
            
            
            
# Main starts here
if __name__ == "__main__":
    # Reading inventory file and building List of Dictionaries
    inventory = read_inventory("Data\inventory.csv")
    print(inventory)
    inv_cost = sum(p["quant"]*p["price"] for p in inventory)
    print("inv_cost:",inv_cost)


        
        
        


