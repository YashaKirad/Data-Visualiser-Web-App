import os

import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import streamlit as st 

#Page Config

st.set_page_config(page_title="Data Visualiser", layout="centered", page_icon="📊")

#Title
st.title("Data Vizualiser 📊")

#Working dir
working_dir=os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

#list files in data
files_list = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

#Dropdown
selected_file=st.selectbox("Select a file",files_list,index=None) 
##None so that no file choosen by default

#

