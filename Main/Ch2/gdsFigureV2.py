# pip install git+https://github.com/Aypac/GDSLatexConverter.git
# pip install wand
from pathlib import Path

# Get the path of the executed file
file_path = Path(Path(__file__).parent, 'gds', 'DC_DieBTest_V2.GDS')

# Print the directory containing the executed file
print(file_path)

import gdspy
from GDSLatexConverter import GDSLatexConverter
gdsii = gdspy.GdsLibrary()

lib = gdsii.read_gds(infile=str(file_path))
gds_smaller = gdspy.GdsLibrary()
gds_smaller.add(gdsii.cell_dict['BP_2x2'])
gds_smaller.add(gdsii.cell_dict['BP'])
gds_smaller.add(gdsii.cell_dict['LED_MESA_100um'])
# conv.textype = GDSLatexConverter.PDFLATEX
conv2 = GDSLatexConverter(gds_smaller)
conv2.scale = 0.0025
print(conv2.all_layer)

def save_and_plot(converter, filename):
    converter.compile(filename=filename, overwrite=True)

    # Show the output pdf
    try:
        from wand.image import Image as WImage
        img = WImage(filename=filename + '.pdf')
        img.rotate(90)
    except:
        img = 'PDF could not be displayed. Please install the library wand (pip install wand).'
    return img

conv2.scale = 0.003 #Set a convienient scale for line-thickness
colorscheme = {
        0: 'yellow',
        1: 'green',
        2: 'red',
        3: 'blue',
        4: 'purple',
}
drawopt = {
        0: 'line width=1, pattern=north west lines, pattern color=yellow!30',
        1: 'line width=1, pattern=north west lines, pattern color=green!15',
        2: 'line width=1, pattern=north west lines, pattern color=red!30, ',
        3: 'line width=1, pattern=north east lines, pattern color=blue!15,',
        4: 'pattern=north east lines, pattern color=violet!10,',
}
conv2.layer_drawopt = drawopt
conv2.layer_drawcolor = colorscheme

save_and_plot(converter=conv2,
              filename=str(Path(file_path.parent, str(file_path.name) + 'tex_output')))

gds_12um = gdspy.GdsLibrary()
gds_12um.add(gdsii.cell_dict['LED1'])
gds_12um.add(gdsii.cell_dict['LED_MESA_100um'])
conv3 = GDSLatexConverter(gds_12um)
conv3.scale = 0.0025

conv3.layer_drawopt = drawopt
conv3.layer_drawcolor = colorscheme
save_and_plot(converter=conv2,
              filename=str(Path(file_path.parent, str(file_path.stem) + '12um_tex_output')))
