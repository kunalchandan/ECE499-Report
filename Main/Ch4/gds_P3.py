# pip install git+https://github.com/Aypac/GDSLatexConverter.git
# pip install wand
from pathlib import Path

# Get the path of the executed file
file_path = Path(Path(__file__).parent, 'gds', 'ONOFF_NC_2022_V3.GDS')

# Print the directory containing the executed file
print(file_path)

import gdspy
from GDSLatexConverter import GDSLatexConverter
colorscheme = {
        0: 'yellow',
        2: 'green',
        21: 'red',
        22: 'blue',
        23: 'purple',
        24: 'blue',
}
drawopt = {
        0: 'line width=1, pattern=north west lines, pattern color=yellow!30',
        2: 'line width=1, pattern=north west lines, pattern color=green!15',
        21: 'line width=1, pattern=north west lines, pattern color=red!30, ',
        22: 'line width=1, pattern=north east lines, pattern color=blue!15,',
        23: 'pattern=north east lines, pattern color=violet!10,',
        24: 'pattern=north east lines, pattern color=blue!10,',
}


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

gdsii = gdspy.GdsLibrary()

lib = gdsii.read_gds(infile=str(file_path))
s_gds_1 = gdspy.GdsLibrary()
s_gds_2 = gdspy.GdsLibrary()
s_gds_3 = gdspy.GdsLibrary()

s_gds_1.add(gdsii.cell_dict['LED_BP_Overlay'])
s_gds_1.add(gdsii.cell_dict['LED_CHIP_10x10'])
s_gds_1.add(gdsii.cell_dict['ONOFF_BP_CHIP_10x10'])
s_gds_1.add(gdsii.cell_dict['LED_nContact_Bump'])
s_gds_1.add(gdsii.cell_dict['AM'])
s_gds_1.add(gdsii.cell_dict['Bonding Alignment Mark'])
s_gds_1.add(gdsii.cell_dict['LED_MESA_100um'])
s_gds_1.add(gdsii.cell_dict['N_Trace'])
s_gds_1.add(gdsii.cell_dict['BP_Bump_LEDside'])
s_gds_1.add(gdsii.cell_dict['BP_Bump_nside'])
s_gds_1.add(gdsii.cell_dict['P_Trace'])
s_gds_1.add(gdsii.cell_dict['center'])
s_gds_1.add(gdsii.cell_dict['full$side'])
s_gds_1.add(gdsii.cell_dict['corner'])
s_gds_1.add(gdsii.cell_dict['one$side'])
s_gds_1.add(gdsii.cell_dict['corner$bit'])
s_gds_1.add(gdsii.cell_dict['side$bit'])

s_gds_2.add(gdsii.cell_dict['ONOFF_BP_CHIP_10x10'])
s_gds_2.add(gdsii.cell_dict['Bonding Alignment Mark'])
s_gds_2.add(gdsii.cell_dict['N_Trace'])
s_gds_2.add(gdsii.cell_dict['P_Trace'])
s_gds_2.add(gdsii.cell_dict['BP_Bump_LEDside'])
s_gds_2.add(gdsii.cell_dict['BP_Bump_nside'])

s_gds_3.add(gdsii.cell_dict['LED_CHIP_10x10'])
s_gds_3.add(gdsii.cell_dict['LED_nContact_Bump'])
s_gds_3.add(gdsii.cell_dict['AM'])
s_gds_3.add(gdsii.cell_dict['Bonding Alignment Mark'])
s_gds_3.add(gdsii.cell_dict['LED_MESA_100um'])
s_gds_3.add(gdsii.cell_dict['center'])
s_gds_3.add(gdsii.cell_dict['full$side'])
s_gds_3.add(gdsii.cell_dict['corner'])
s_gds_3.add(gdsii.cell_dict['one$side'])
s_gds_3.add(gdsii.cell_dict['corner$bit'])
s_gds_3.add(gdsii.cell_dict['side$bit'])

# conv.textype = GDSLatexConverter.PDFLATEX
conv_3 = GDSLatexConverter(s_gds_3)
conv_3.scale = 0.0025
conv_3.layer_drawopt = drawopt
conv_3.layer_drawcolor = colorscheme
print(conv_3.all_layer)

save_and_plot(converter=conv_3,
              filename=str(Path(file_path.parent, str(file_path.name) + '_LED')))
conv_2 = GDSLatexConverter(s_gds_2)
conv_2.scale = 0.0025
conv_2.layer_drawopt = drawopt
conv_2.layer_drawcolor = colorscheme
print(conv_2.all_layer)

save_and_plot(converter=conv_2,
              filename=str(Path(file_path.parent, str(file_path.name) + '_BP')))
conv_1 = GDSLatexConverter(s_gds_1)
conv_1.scale = 0.0025
conv_1.layer_drawopt = drawopt
conv_1.layer_drawcolor = colorscheme
print(conv_1.all_layer)

save_and_plot(converter=conv_1,
              filename=str(Path(file_path.parent, str(file_path.name) + '_BOTH')))
