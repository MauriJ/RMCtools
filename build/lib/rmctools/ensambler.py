#%%

import numpy as np
from CifFile import ReadCif, CifBlock

#%%

cf = ReadCif('../data/Cu.cif')
print(cf)

#%%

print(cf['4105040']['_geom_angle'])

# cf['4105040'].keys()