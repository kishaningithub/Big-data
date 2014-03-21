#!/usr/bin/python

import sys
import csv

oldKey = None
nodeNames =[]

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader:
    data_mapped=line
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
        writer.writerow([oldKey,len(nodeNames),",".join(set(nodeNames))])
        oldKey = thisKey;
        nodeNames=[]

    oldKey = thisKey
    nodeNames.append(thisVal)

if oldKey != None:
    writer.writerow([oldKey,len(nodeNames),",".join(set(nodeNames))])

