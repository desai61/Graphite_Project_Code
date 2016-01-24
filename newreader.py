import xlrd
import numpy as np
import scipy.spatial.distance as s
import curvegenerator as c
#np.set_printoptions(suppress=True)
#np.set_printoptions(threshold=1000)
array = np.zeros((85626,4))
book = xlrd.open_workbook("D:\Purdue\Research\Pythonscripts\coords.xlsx")
sheet = book.sheet_by_index(0)

######## WRITING DATA FILE ##########
target = open("bonds.txt", 'w')
target.write("\nBonds\n\n")

for i in range(85626):
    array[i,0] = sheet.cell(i,0).value
    array[i,1] = sheet.cell(i,3).value
    array[i,2] = sheet.cell(i,4).value
    array[i,3] = sheet.cell(i,5).value

leftedge = []
rightedge = []
for i in range(len(array[:,1])):
    if (array[i,1] == 0):
        leftedge.append(i+1)  
    if(array[i,1] >= 245.3 and array[i,1] <= 245.37):
        rightedge.append(i+1)

length = len(leftedge)
count = 0
for i in range(length):
     count += 1
     target.write('{}'.format(count)+' {}'.format(1)+' {}'.format(leftedge[i])+' {}'.format(rightedge[i])+"\n")

length = len(array[:,1])
nearint = int(length/100)

for idx in range(1,101):
    print(idx)
    if (idx == 1):
        dist = s.pdist(array[(idx-1)*nearint:idx*nearint,1:])
        dist = s.squareform(dist)
        for i in range(nearint):
            for j in range(nearint):
                if ((dist[i][j] >= 1.4 and dist[i][j] <= 1.5) and i<j ):
                    count += 1
                    target.write('{}'.format(count)+' {}'.format(1)+
                    ' {}'.format(i+1+(idx-1)*nearint)+' {}'.format(j+1+(idx-1)*nearint)+"\n")
    else:
        dist = s.pdist(array[(idx-1)*nearint-200:idx*nearint,1:])
        dist = s.squareform(dist)
        for i in range(nearint+200):
            for j in range(nearint+200):
                if ((dist[i][j] >= 1.4 and dist[i][j] <= 1.5) and i<j ):
                    count += 1
                    target.write('{}'.format(count)+' {}'.format(1)+
                    ' {}'.format(i+1+(idx-1)*nearint-200)+' {}'.format(j+1+(idx-1)*nearint-200)+"\n")

dist = s.pdist(array[100*nearint:,1:])
dist = s.squareform(dist)

for i in range(length%100):
    for j in range(length%100):
        if ((dist[i][j] >= 1.4 and dist[i][j] <= 1.5) and i<j ):
            count += 1
            target.write('{}'.format(count)+' {}'.format(1)+' {}'.format(i+1+(100*nearint))
            +' {}'.format(j+1+(100*nearint))+"\n")

target.close()