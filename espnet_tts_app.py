# Entry point file for pyinstaller

# workaround for 'No module named streamlit.runtime.scriptrunner.magic_funcs'
import streamlit.runtime
import streamlit.runtime.scriptrunner
import streamlit.runtime.scriptrunner.magic_funcs

import streamlit.web.cli as stcli
import sys

# for pyinstaller
import numpy
import scipy
import librosa
import streamlit
import soundfile
#import st_aggrid
#import stqdm

import time
import torch
import matplotlib 

import jamo
import espnet
import espnet2
import espnet2.bin.tts_inference
import espnet2.utils.types

import torch

import os

def streamlit_run():
    sys.argv=["streamlit", "run", "espnet_tts_app_streamlit.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    streamlit_run()
