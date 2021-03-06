
import numpy as np
import pynbody as pb
import astropy.units as u
import os
import KeplerOrbit as ko


import glob
import re

files = glob.glob1('.','asteroids_low.[0-9]*[0-9]')

# Sort files according to the digits included in the filename
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
max_mass = []
mean_mass = []
times = []
n_particles = []
stepnumber = []
for filename in files:
        snap1 = pb.load (filename)
        snap = ko.orb_params(snap1)
       
    #max mass
        max_mass.append(np.max(snap['mass']))
    #average mass
        mean_mass.append(np.mean(snap['mass']))

    #time
        times.append(snap.properties['time'].in_units('yr'))
        print(filename)
        
        n_particles.append(len(snap1))
        
        stepnumber.append(int(filename.split('.')[1]))
              #saving
np.savetxt('time_mass.txt', [times, max_mass, mean_mass, n_particles, stepnumber])



#not sure what this one does or what it splits
#f.split('.')[1]

 
#list of how many particles in snapshot( why do i need to know how many particles?)
len(snap)

#find time and mass to plot but here to find time and max mass and avg mass
#extra: snap1 = pb.load ('asteroids_low.24680000')
#snap = ko.orb_params(snap1)
#in terminal before do: 
# ls -1v asteroids_low.[0-9]*[0-9] | sort -nr > files.txt