import numpy as np
la= 2.4534 #xdir
lb = 4.2492 #ydir
lc = 5  #outofplane lattice parameter
 
nrx = 2 #number of unit cells in x
nry = 2 #number of unit cells in y
ns = 2 #number of sheets
na = 0 #number of atoms
nuc = nrx*nry*ns
coords = np.zeros((nuc,4,3)) #nrx*nry*ns*4 is the no. of atoms in the horizontal sheets

#==============================================================================
# def eqz(y,z):
#     if(z<lc/2):
#         ans = lc/2 - np.sqrt((lc/2)**2 - (y-nry*lb)**2)
#     if(z>lc/2):
#         ans = lc/2 + np.sqrt((lc/2)**2 - (y-nry*lb)**2)
#     return ans 
#==============================================================================

######## WRITING DATA FILE ##########
target = open("test.txt", 'w')
target.write("\n")
target.write('{}'.format(1)+" atom types\n\n")
target.write('{}'.format(0.0)+ ' {}'.format(la*nrx)+ " xlo xhi\n")
target.write('{}'.format(0.0)+ ' {}'.format(lb*nry)+ " ylo yhi\n")
target.write('{}'.format(0.0)+ ' {}'.format(lc*ns)+ " zlo zhi\n\n")
target.write("Masses\n\n")
target.write('{}'.format(1)+' {}'.format(12)+"\n\n")
target.write("Atoms\n\n")

####### HORIZONTAL SHEETS ########
i = 0
for z in range(0,ns):
    for x in range(0,nrx):
        for y in range(0,nry): #for each unit cell
            coords[i,0,:] = np.array([(0+x)*la,(0+y)*lb,z*lc])
            na+=1
            print coords[i,0,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,0,0])+' {}'.format(coords[i,0,1])+' {}'.format(coords[i,0,2])+"\n")
            coords[i,1,:] = np.array([(1/2.+x)*la,(1/6.+y)*lb,z*lc])
            na+=1
            print coords[i,1,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,1,0])+' {}'.format(coords[i,1,1])+' {}'.format(coords[i,1,2])+"\n")                
            coords[i,2,:] = np.array([(1/2.+x)*la,(1/2.+y)*lb,z*lc])
            na+=1
            print coords[i,2,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,2,0])+' {}'.format(coords[i,2,1])+' {}'.format(coords[i,2,2])+"\n")
            coords[i,3,:] = np.array([(1+x)*la,(2/3.+y)*lb,z*lc])
            na+=1
            print coords[i,3,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,3,0])+' {}'.format(coords[i,3,1])+' {}'.format(coords[i,3,2])+"\n")
            i+=1


########## VERTICAL SHEETS ########
nrz = int(lc/la) #number of unit cells in x
nuc = nrz*nry*(ns-1)
newcoords = np.zeros((nuc,4,3))
i = 0

for currsheet in range(0,ns-1): #ns-1 as we don't want to create a sheet perpendicular to the last one
    if (currsheet%2==0):
        sheetvar = 1 #set xcoordinate for right vertical sheet
    else:
        sheetvar = 0  #set xcoordinate for left vertical sheet        
    for z in range(0,nrz):
        for y in range(0,nry): #for each unit cell
            newcoords[i,0,:] = np.array([sheetvar*la*nrx,(0+y)*lb,(0+z)*la]) + np.array([0,0,currsheet*lc])
            na+=1
            print newcoords[i,0,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,0,0])+' {}'.format(newcoords[i,0,1])+' {}'.format(newcoords[i,0,2])+"\n")
            newcoords[i,1,:] = np.array([sheetvar*la*nrx,(1/6.+y)*lb,(1/2.+z)*la]) + np.array([0,0,currsheet*lc])
            na+=1
            print newcoords[i,1,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,1,0])+' {}'.format(newcoords[i,1,1])+' {}'.format(newcoords[i,1,2])+"\n")                
            newcoords[i,2,:] = np.array([sheetvar*la*nrx,(1/2.+y)*lb,(1/2.+z)*la]) + np.array([0,0,currsheet*lc])
            na+=1
            print newcoords[i,2,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,2,0])+' {}'.format(newcoords[i,2,1])+' {}'.format(newcoords[i,2,2])+"\n")
            newcoords[i,3,:] = np.array([sheetvar*la*nrx,(2/3.+y)*lb,(1+z)*la]) + np.array([0,0,currsheet*lc])
            na+=1
            print newcoords[i,3,:]
            target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,3,0])+' {}'.format(newcoords[i,3,1])+' {}'.format(newcoords[i,3,2])+"\n")
            i+=1
            print "i=", i

target.write('{}'.format(na)+" atoms\n")
target.close()            







