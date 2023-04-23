import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


df = pd.read_csv('dataWidthMap.txt', delimiter='&', header=None)
def clean(x: str) -> str:
    return x.strip().replace('\\grd{', '').replace('}', '').replace('\\', '')
df = df.applymap(clean)

# Get Min and max of dataset
vmin = 10000000
vmax = 0
for ii, aa in enumerate(df.to_numpy()):
    for jj, bb in enumerate(aa):
        if bb != '':
            bb = np.log(float(bb))
            if bb < vmin:
                vmin = bb
            if bb > vmax:
                vmax = bb

class colour:
    def __init__(self, rgba: Tuple[float, float, float, float]) -> None:
        self.r = int(rgba[0]*255)
        self.g = int(rgba[1]*255)
        self.b = int(rgba[2]*255)
        self.a = int(rgba[3]*255)

# Generate text drawings and colours
cellsize = 1
for ii, aa in enumerate(df.to_numpy()):
    for jj, bb in enumerate(aa):
        if bb != '':
            csz = ' * \\cSz'
            strii = str( ((ii+0.5*cellsize)/cellsize) ).zfill(2) + csz
            strjj = str( ((jj+0.5*cellsize)/cellsize) ).zfill(2) + csz
            r1_ii = str( (ii/cellsize) ).zfill(2) + csz
            r1_jj = str( (jj/cellsize) ).zfill(2) + csz
            r2_ii = str( ((ii+cellsize)/cellsize) ).zfill(2) + csz
            r2_jj = str( ((jj+cellsize)/cellsize) ).zfill(2) + csz
            # print(color)
            magnitude = ((np.log(float(bb)) - vmin)/(vmax-vmin))*90
            print(f'\\draw[fill=purple4!{magnitude:0.1f}, draw] ({r1_ii}, {r1_jj}) rectangle ({r2_ii}, {r2_jj});')
            print(f'\\node at ({strii}, {strjj}) ',  '{', bb, '};')
