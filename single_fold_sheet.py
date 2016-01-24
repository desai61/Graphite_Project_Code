import numpy as np
la= 2.4534    #xdir
lb = 4.2492   #ydir
lc = 3.6801  #outofplane lattice parameter

bl = 1.416    #Bond length of carbon-carbon 
nrx = 25      #number of unit cells in x
nry = 25     #number of unit cells in y
ns = 2       #number of sheets
na = 0        #initial number of atoms
nuc = nrx*nry*ns
coords = np.zeros((nuc,4,3)) #nrx*nry*ns*4 is the no. of atoms in the horizontal sheets

######## WRITING DATA FILE ##########
target = open("datafile.txt", 'w')
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
sheetvar = 0
for z in range(0,ns):     
    line = 0
    x = 0
    y = 0
    while(x < nrx*la):
        if (line%2 == 0):
            y = 0
            while (y < nry*lb):
                coords[i,0,:] = np.array([(line/2.)*la+sheetvar,y,z*lc])
                na+=1
                print coords[i,0,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,0,0])+' {}'.format(coords[i,0,1])+' {}'.format(coords[i,0,2])+"\n")           
                y += bl
                coords[i,1,:] = np.array([(line/2.)*la+sheetvar,y,z*lc])
                na+=1
                print coords[i,1,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,1,0])+' {}'.format(coords[i,1,1])+' {}'.format(coords[i,1,2])+"\n")           
                y += 2*bl
        else:
            y = bl+bl/2
            while (y < nry*lb):
                coords[i,2,:] = np.array([(line/2.)*la+sheetvar,y,z*lc])
                na+=1
                print coords[i,2,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,2,0])+' {}'.format(coords[i,2,1])+' {}'.format(coords[i,2,2])+"\n")           
                y += bl
                coords[i,3,:] = np.array([(line/2.)*la+sheetvar,y,z*lc])
                na+=1
                print coords[i,3,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[i,3,0])+' {}'.format(coords[i,3,1])+' {}'.format(coords[i,3,2])+"\n")           
                y += 2*bl
        i += 1
        line += 1
        x += la/2
    sheetvar += la/2

####### VERTICAL SHEETS ########
nrz = int(lc/la)+1 #number of unit cells in x
nuc = nrz*nry*(ns-1)
newcoords = np.zeros((nuc,4,3))
i = 0

for currsheet in range(0,ns-1): #ns-1 as we don't want to create a sheet perpendicular to the last one
    if (currsheet%2==0):
        sheetvar = la*nrx #set xcoordinate for right vertical sheet
    else:
        sheetvar = la/2  #set xcoordinate for left vertical sheet        
    line = 0
    z = 0
    y = 0
    while(z < nrz*la-la/2):
        if (line%2 == 0):
            y = 0
            while (y < nry*lb):
                newcoords[i,0,:] = np.array([sheetvar,y,(line/2.)*la]) + np.array([0,0,currsheet*lc])
                na+=1
                print newcoords[i,0,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,0,0])+' {}'.format(newcoords[i,0,1])+' {}'.format(newcoords[i,0,2])+"\n")           
                y += bl
                newcoords[i,1,:] = np.array([sheetvar,y,(line/2.)*la]) + np.array([0,0,currsheet*lc])
                na+=1
                print newcoords[i,1,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,1,0])+' {}'.format(newcoords[i,1,1])+' {}'.format(newcoords[i,1,2])+"\n")           
                y += 2*bl
        else:
            y = bl+bl/2
            while (y < nry*lb):
                newcoords[i,2,:] = np.array([sheetvar,y,(line/2.)*la]) + np.array([0,0,currsheet*lc])
                na+=1
                print newcoords[i,2,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,2,0])+' {}'.format(newcoords[i,2,1])+' {}'.format(newcoords[i,2,2])+"\n")           
                y += bl
                newcoords[i,3,:] = np.array([sheetvar,y,(line/2.)*la]) + np.array([0,0,currsheet*lc])
                na+=1
                print newcoords[i,3,:]
                target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(newcoords[i,3,0])+' {}'.format(newcoords[i,3,1])+' {}'.format(newcoords[i,3,2])+"\n")           
                y += 2*bl
        i += 1
        line += 1
        z += la/2
        
target.write('{}'.format(na)+" atoms\n")
target.close()         