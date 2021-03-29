
#!/bin/python
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import math
import os
import random
import re
import sys

def maxProfit(self, prices):
    maxProfit = -1
    bottom = sys.maxint

    if (len(prices) <= 1):
        return 0

    for i in range(0,len(prices)):
        if (prices[i] < bottom):
            bottom = prices[i]
        elif ( prices[i]- bottom > maxProfit):
            maxProfit = prices[i]- bottom
    if (maxProfit < 0):
        return 0
    return maxProfit





        
if __name__ == '__main__':
    

    prices = map(int, raw_input().rstrip().split())
        
    print (str(maxProfit(prices)))
    
