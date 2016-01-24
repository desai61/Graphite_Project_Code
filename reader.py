import xlrd
import numpy as np
import scipy.spatial.distance as s
#np.set_printoptions(suppress=True)
#np.set_printoptions(threshold=1000)
array = np.zeros((7920,4))
book = xlrd.open_workbook("D:\Purdue\Research\Pythonscripts\coords.xlsx")
sheet = book.sheet_by_index(0)

######## WRITING DATA FILE ##########
target = open("bonds.txt", 'w')
target.write("\nBonds\n\n")

for i in range(7920):
    array[i,0] = sheet.cell(i,0).value
    array[i,1] = sheet.cell(i,3).value
    array[i,2] = sheet.cell(i,4).value
    array[i,3] = sheet.cell(i,5).value

leftedge = []
rightedge = []
for i in range(len(array[:,1])):
    if (array[i,1] == 0):
        leftedge.append(i+1)  
    if(array[i,1] >= 72.36 and array[i,1] <= 72.38):
        rightedge.append(i+1)

length = len(leftedge)
count = 0
for i in range(length):
     count += 1
     target.write('{}'.format(count)+' {}'.format(1)+' {}'.format(leftedge[i])+' {}'.format(rightedge[i])+"\n")

dist = s.pdist(array[:,1:])
dist = s.squareform(dist)
        
for i in range(7920):
    print i
    for j in range(i+1):
        if ((dist[i][j] >= 1.4 and dist[i][j] <= 1.5)):
            count += 1
            target.write('{}'.format(count)+' {}'.format(1)+
            ' {}'.format(i+1)+' {}'.format(j+1)+"\n")
            
target.close()