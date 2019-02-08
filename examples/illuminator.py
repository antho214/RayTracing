import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from ABCD import *

path = OpticalPath()
path.name = "Kohler illumination with 1 cm wide lamp and 0.5 NA"
path.objectHeight = 1.0
path.fanAngle = 0.5
path.rayNumber = 3
path.append(Space(d=4))
path.append(Lens(f=4,diameter=2.5))
path.append(Space(d=4+25))
path.append(Lens(f=25, diameter=7.5))
path.append(Space(d=20))
path.append(Space(d=5))
path.append(Space(d=9))
path.append(Lens(f=9, diameter=8))
path.append(Space(d=9))

print(path.fieldStop())
print(path.fieldOfView())
path.display(onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)
path.save("Illumination.png",onlyChiefAndMarginalRays=True, limitObjectToFieldOfView=True)