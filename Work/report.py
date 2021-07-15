"""  

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
                inventory.append({headers[0]:row[0],headers[1]:int(row[1]),headers[2]:float(row[2])})
            i += 1
    except FileNotFoundError:
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return inventory
            
def read_prices(filename):
    try:
        prices = dict()
        with open(filename) as FH:
            rows = csv.reader(FH)
            for row in rows:
                try:
                    prices[row[0]] = float(row[1])
                except ValueError as e:
                    print("Bad row",row)
                    print("Reason:",e)
                except IndexError as m:
                    print("Skipping blank line....")
    except FileNotFoundError:
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return prices
 
            
# Main starts here
if __name__ == "__main__":
    # Reading inventory file and building List of tuples
    inventory = read_inventory("Data\inventory.csv")
    curr_inv_cost = sum(p["quant"]*p["price"] for p in inventory)
    print("Total cost:",curr_inv_cost)
    
    # Reading latest price file and building alist of Dictionary
    prices = read_prices("Data\prices.csv")
    new_inv_cost = 0.0
    
    # Compute present value of inventory
    for p in inventory:
            if p['name'] in list(prices):
                idx = list(prices).index(p['name'])
                new_inv_cost += p['quant']*prices[p['name']]
    print("Present Value:",new_inv_cost)
    
    # Printing Total Gain/Loss
    print("Total Gain:",new_inv_cost - curr_inv_cost)



        
        
        


