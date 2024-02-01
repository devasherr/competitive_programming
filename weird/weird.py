#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
  
    # instad of writing manually we can make a list for the numbers  
    weirdNums = [i for i in range(6, 21)]
    
    if n % 2 != 0:
        print("Weird")
    elif n in weirdNums:
        print("Weird")
    else:
        print("Not Weird")  
    
