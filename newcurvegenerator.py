import numpy as np

la= 2.4534    #lattice constant in xdir
bl = 1.4164   #Bond length (carbon-carbon)

######## USER INPUTS ########
nrx = 2     #Number of repeat units in x dir (actual will have nrx - 0.5)
R = 2     #Radius of sheet (circular cap)
#L = 2.832*25  #Length in y dir (prefer multiple of 2*bl to not leave dangling bonds)
nry = 2    
na = 0        #initial number of atoms
coords = []   #Coordinate list

target = open("curvedatafile.txt", 'w')

def eq(ystart, zstart, zend, yend, y):
    slope = (zend - zstart)/(yend - ystart)
    z = zstart + slope*y
    return z

########## FUNCTION TO WRITE COORDINATES (most recently added) ############## 
def write_coords(coords, na):
    target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[len(coords)-1][0])
    +' {}'.format(coords[len(coords)-1][1])+' {}'.format(coords[len(coords)-1][2])+"\n")

########### SORTING FUNCTION ##################
def insort(a, b, kind='mergesort'):
    # took mergesort as it seemed a tiny bit faster for my sorted large array try.
    c = np.concatenate((a, b)) # we still need to do this unfortunatly.
    c.sort(kind=kind)
    return c

################# HORIZONTAL SHEETS #################
def horizontal_sheet(xstart, ystart, xlength, nry, zstart, zend, na):
    x = xstart
    theta = np.pi/6
    y1 = np.arange(ystart,nry*3*bl*np.cos(theta),3*bl*np.cos(theta))
    y2 = np.arange(ystart+bl,nry*3*bl*np.cos(theta),3*bl*np.cos(theta))
    y3 = insort(y1,y2)
    y4 = y3 + 3*bl/2
    ylen = len(y3)
    yend = y4[ylen-1]
    i = 0
    while(x < xlength):
        if (i%2 == 1):
            coords.append([x,ystart,eq(ystart, zstart, zend, yend, ystart)])
            na += 1
            write_coords(coords, na)
        for j in range(ylen):
            if(i%2 == 0):
                coords.append([x,y3[j],eq(ystart, zstart, zend, yend, y3[j])])
                na += 1
                write_coords(coords, na)
            else:                
                coords.append([x,y4[j],eq(ystart, zstart, zend, yend, y4[j])])
                na += 1
                write_coords(coords, na)
        if (i%2 == 0):
            coords.append([x,y4[ylen-1]+bl/2,eq(ystart, zstart, zend, yend, y4[ylen-1]+bl/2)])
            na += 1
            write_coords(coords, na)
        i += 1
        x += la/2
        
    yend = y4[ylen-1]
    xend = x - la/2
    return xend, yend, zend, na
    
################ CAP FUNCTION ########################
def cap(xstart, ystart, z, na):
    switch = 1
    count = 0
    x = xstart
    ystart = ystart
    angle = np.arccos(1 - (bl*bl)/(2*R*R))
    while(x < nrx*la):
        count += 1
        theta = 0 + switch*(np.arccos(1 - (bl*bl)/(2*R*R*4)))
        while(theta < np.pi):
            coords.append([x, -R*np.sin(theta)+ystart,R*np.cos(theta)+z-R])
            na += 1
            write_coords(coords, na)
            theta += (angle + (1-switch)*angle)
            coords.append([x, -R*np.sin(theta)+ystart,R*np.cos(theta)+z-R])
            na += 1
            write_coords(coords, na)
            yend_cap = -R*np.sin(theta) + ystart
            zend_cap = R*np.cos(theta) + z - R
            theta += (2*angle - (1-switch)*angle)
        x += la/2
        switch = 1 - switch
    return yend_cap, zend_cap, na

############## FUNCTION CALLS ################
xhor, yhor, zhor, na = horizontal_sheet(0,0,nrx*la,nry,10,0,na)
#yend_cap, zend_cap, na = cap(0,0,0,na)
#xhor, yhor, zhor, na = horizontal_sheet(0,yend_cap+2*bl/2,nrx*la,nry,zend_cap,na)

############ FILE WRITING #######################
target.write("\n")
target.write('{}'.format(na)+" atoms\n")
target.write('{}'.format(1)+" atom types\n\n")
target.write('{}'.format(min(list(zip(*coords))[0]))+ ' {}'.format(max(list(zip(*coords))[0])+la/2)+ " xlo xhi\n")
target.write('{}'.format(min(list(zip(*coords))[1]))+ ' {}'.format(max(list(zip(*coords))[1]))+ " ylo yhi\n")
target.write('{}'.format(min(list(zip(*coords))[2]))+ ' {}'.format(max(list(zip(*coords))[2]))+ " zlo zhi\n")
target.write("\nMasses\n\n")
target.write('{}'.format(1)+' {}'.format(12)+"\n\n")
target.write("Atoms\n\n")
target.close()            