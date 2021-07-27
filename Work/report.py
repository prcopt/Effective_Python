"""  
WORKING WITH DATA: Inventory Report Generation - Q12
"""
import sys
import csv
import pathlib
from product import Product
def read_inventory(filename):
    try:
        inventory = list()
        with open(filename) as FH:
            rows = csv.reader(FH)
            headers = next(rows)
            for row_no,row in enumerate(rows,start=1):
                try:
                    values = row
                    prod = dict(zip(headers,values))
                    prod['quant'] = int(prod['quant'])
                    prod['price'] = float(prod['price'])
                    probj =Product(prod['name'],prod['quant'],prod['price'])
                    inventory.append(probj)
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
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return inventory
            
def read_prices(filename):
    try:        
        prices = dict()
        with open(filename) as FHR:
            rows = csv.reader(FHR)
            header = ['name','price']
            for row in rows:
                try:
                    values = row
                    set = dict(zip(header,values))
                    prices[set['name']] = float(set['price'])
                except ValueError as e:
                    print("Bad row",row)
                    print("Reason:",e)
                except IndexError as m:
                    print("Skipping blank line....")
    except FileNotFoundError:
        print("File:",filename, "Not Found: Execution Terminated.")
        sys.exit("")
    return prices

""" make_report function build a table that contain product name, qty, Original price and change of price
     input: product ( current inventory) and new price list.
     output: table containg items as above.
"""
def make_report(inventory,prices):
    new_price = list()
    change = list()
    for p in inventory:
        if p.name in prices:
            new_price.append(prices[p.name])
            change.append(prices[p.name]- p.price)
    table = [(p.name,p.quant,np,c) for p,np,c in zip(inventory,new_price,change)]
    return table

# Main starts here
if __name__ == "__main__":
    # Reading inventory file and building List of tuples
    inventory = read_inventory("Data\inventorydate.csv")
    curr_inv_cost = sum(int(p.quant)* float(p.price) for p in inventory)
    print("Total cost:",curr_inv_cost)

    # Reading latest price file and building alist of Dictionary
    prices = read_prices("Data\\prices.csv")
    new_inv_cost = 0.0
    
    # Compute present value of inventory
    for p in inventory:
            if p.name in prices:
                new_inv_cost += p.quant* prices[p.name]
    print("Present Value:",new_inv_cost)
    
    # Printing Total Gain/Loss
    print("Total Gain:",new_inv_cost - curr_inv_cost)

    # Making formatted Report
    report = make_report(inventory,prices)
    headers = ("Name","Quantity","Price","Change")
    st = ""
    for i in headers:
        st += i.rjust(10)+" "
    print(st)
    print(f'{"":->10} {"":->10} {"":->10} {"":->10}')

    for r in report:
        print(f'{r[0]:>10s} {int(r[1]):>10d} {r[2]:>10.2f} {r[3]:>10.2f}')
    print()
    print(st)
    print(f'{"":->10} {"":->10} {"":->10} {"":->10}')
    for r in report:
        price = '\u20B9'+ str(r[2])    
        print(f'{r[0]:>10s} {int(r[1]):>10d} {price:>10s} {r[3]:>10.2f}')    
        
        
        


