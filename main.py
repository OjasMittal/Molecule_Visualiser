import streamlit as st
import glob
from st_speckmol import speck_plot
st.title('Molecule Analyser')
st.subheader('A tool to analyse various molecule structures :microscope: ')
st.write("")
ex_files = glob.glob("xyz_mol_examples/*.xyz")
with st.sidebar:
    example_xyz = st.selectbox("Select a molecule",ex_files)
    f = open(example_xyz,"r")
    example_xyz = f.read()
    st.sidebar.info(example_xyz.splitlines()[1])
with st.sidebar.expander("Advanced Settings",expanded=True):
    outl = st.checkbox('Outline',value=True)
    bond = st.checkbox('Bond',value=True)
    bond_scale = st.slider('BondScale',min_value=0.0,max_value=1.0,value=0.8)
    brightness = st.slider('Brightness',min_value=0.0,max_value=1.0,value=0.4)
    relativeAtomScale = st.slider('RelativeAtomScale',min_value=0.0,max_value=1.0,value=0.64)
    bondShade = st.slider('bondShade',min_value=0.0,max_value=1.0,value=0.5)
st.info('Use sidebar to select different structures and to apply customisations')
_PARAMETERS = {'outline': outl , 'bondScale': bond_scale,
                'bonds': bond ,'bondShade' : bondShade,
                'brightness': brightness, 'relativeAtomScale':relativeAtomScale,
                }
res = speck_plot(example_xyz,_PARAMETERS = _PARAMETERS,wbox_height="500px",wbox_width="800px")
