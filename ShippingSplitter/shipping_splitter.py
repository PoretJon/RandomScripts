import csv
from os import listdir

def main():
    totalOrders = dict()
    totalBoxesOrdered = 0
    with open('ShippingSplitter/order.csv', 'r') as file:
        reader = csv.DictReader(file)

        for line in reader:
            name = line['Name']
            rumbling = line['rumbling']
            glow = line['glow']
            worker = line['worker']
            total = line['total']
            totalOrders[name] = int(total)
            totalBoxesOrdered += int(total)
            print (f'processed {name} ordering {rumbling} rumbling darts, {glow} glow darts, and {worker} worker style darts. Total for {name} is {total}')
    print(f'Total boxes ordered: {totalBoxesOrdered}')
    shippingCost = input('Enter shipping cost: ')
    for person in totalOrders.keys():
        shippingCostOwed = (totalOrders[person] / totalBoxesOrdered) * float(shippingCost)
        print(f'{person} owes {"{0:.2f}".format(shippingCostOwed)} for shipping')
        
main()