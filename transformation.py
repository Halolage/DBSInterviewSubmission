# This script is to pipe data into our program, transform it, and save it.

import csv
import json
import pandas as pd

def transformationFunc(dataset):
    # initialise header list
    header = []
    rows = []
    
    with open(dataset, 'r') as file:

        csvreader = csv.reader(file)

        
        # next() method returns current header column and moves on next column 
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    # print(header)
    # print(rows)

     
    tmp = ""
    output = {}
    counter = 1
    # looping to count the ticker
    for list in rows:
        # verify if similar to previous ticker
        if list[0] == tmp:
            counter += 1
            output[list[0]] = counter
        else:
            output[list[0]] = 0 # else reset counter for new ticker count
            counter = 1
        tmp = list[0]
    
    output = json.dumps(output) # to make it into json format
    print(output)
    return output

transformationFunc("dataset1.csv")
