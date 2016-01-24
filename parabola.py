import numpy as np

la= 2.4534    #lattice constant in xdir
bl = 1.4164   #Bond length (carbon-carbon)

######## USER INPUTS ########
a = 100   #Number of repeat units in x dir (actual will have nrx - 0.5)
L = 200    #Length of sheet in y dir
######### VARIABLES ###########
R = 2*a
nrx = int(L/la)
na = 0        #initial number of atoms
coords = []   #Coordinate list

target = open("paraboladatafile.txt", 'w')

########## FUNCTION TO WRITE COORDINATES (most recently added) ############## 
def write_coords(coords, na):
    target.write('{}'.format(na)+' {}'.format(1)+' {}'.format(0)+' {}'.format(coords[len(coords)-1][0])
    +' {}'.format(coords[len(coords)-1][1])+' {}'.format(coords[len(coords)-1][2])+"\n")

################ CAP FUNCTION ########################
def cap(xstart, ystart, z, na):
    switch = 1
    x = xstart
    ystart = ystart
    angle = np.arccos(1 - (bl*bl)/(2*R*R))
    while(x < nrx*la):
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

############## FUNCTION CALLS ###############
yend_cap, zend_cap, na = cap(0,0,0,na)

############ FILE WRITING #######################
target.write("\n")
target.write('{}'.format(na)+" atoms\n")
target.write('{}'.format(1)+" atom types\n\n")
target.write('{}'.format(min(zip(*coords)[0]))+ ' {}'.format(max(zip(*coords)[0]))+ " xlo xhi\n")
target.write('{}'.format(min(zip(*coords)[1]))+ ' {}'.format(max(zip(*coords)[1]))+ " ylo yhi\n")
target.write('{}'.format(min(zip(*coords)[2]))+ ' {}'.format(max(zip(*coords)[2]))+ " zlo zhi\n")
target.write("\nMasses\n\n")
target.write('{}'.format(1)+' {}'.format(12)+"\n\n")
target.write("Atoms\n\n")
target.close()            