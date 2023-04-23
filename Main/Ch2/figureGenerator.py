import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


df = pd.read_csv('dataHeightMap.txt', delimiter='&', header=None)
def clean(x: str) -> str:
    return x.strip().replace('\\grd{', '').replace('}', '').replace('\\', '')
# print(df.applymap(clean))
df = df.applymap(clean)

# Get Min and max of dataset
vmin = 10000000
vmax = 0
for ii, aa in enumerate(df.to_numpy()):
    for jj, bb in enumerate(aa):
        if bb != '':
            bb = float(bb)
            if bb < vmin:
                vmin = bb
            if bb > vmax:
                vmax = bb
norm = Normalize(vmin=vmin, vmax=vmax)
cmap = plt.cm.get_cmap('cool')
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])


class colour:
    def __init__(self, rgba: Tuple[float, float, float, float]) -> None:
        self.r = int(rgba[0]*255)
        self.g = int(rgba[1]*255)
        self.b = int(rgba[2]*255)
        self.a = int(rgba[3]*255)

    def __repr__(self) -> str:
        return '{rgb,' + f'{self.r:.2f}:red,{self.g:.2f}:green,{self.b:.2f}:blue' + ',1}'
# Generate text drawings and colours
cellsize = 1
for ii, aa in enumerate(df.to_numpy()):
    for jj, bb in enumerate(aa):
        if bb != '':
            c = colour(sm.to_rgba(float(bb)))
            csz = ' * \\cSz'
            strii = str( ((ii+0.5*cellsize)/cellsize) ).zfill(2) + csz
            strjj = str( ((jj+0.5*cellsize)/cellsize) ).zfill(2) + csz
            r1_ii = str( (ii/cellsize) ).zfill(2) + csz
            r1_jj = str( (jj/cellsize) ).zfill(2) + csz
            r2_ii = str( ((ii+cellsize)/cellsize) ).zfill(2) + csz
            r2_jj = str( ((jj+cellsize)/cellsize) ).zfill(2) + csz
            # print(color)
            magnitude = ((float(bb) - vmin)/(vmax-vmin))*90
            print(f'\\draw[fill=purple4!{magnitude:0.1f}, draw] ({r1_ii}, {r1_jj}) rectangle ({r2_ii}, {r2_jj});')

            print(f'\\node at ({strii}, {strjj}) ',  '{', bb, '};')
            # \fillRGB{255}{255}{0}\node[fill,draw]{{\tt fillRGB: 255,255,0} };
            # print(f'\\fillRGB', '{', c.r, '}{', c.g, '}{', c.b, '}\\node[fill,draw]', '{{\\tt fillRGB: ', f'{c.r},{c.g},{c.b}', '} }')
            # print(f'\\draw[fill=[{c}] ({strii},{strjj}) rectangle ({cellsize},{cellsize});')
            # print(f'\\node at ({strii}.5*\cSz, {strjj}.5*\cSz)', ' {', bb, '};')
