
import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self,num_items,item_price):
        self.num_items=num_items
        self.item_price=item_price
        
    def buy(self,req_items,money):
        self.req_itmes= req_items
        self.money = money
        grandprice = req_items * self.item_price
        if (self.num_items >= req_items and grandprice <= money):
            self.num_items = self.num_items - req_items
            return(money - grandprice)
            
        elif req_items > self.num_items:
            return("Not enough items in the machine")
        else:
            return("Not enough coins")
            
    
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()