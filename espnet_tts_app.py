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
#import st_aggrid
#import stqdm

import torch

import os

def streamlit_run():
    sys.argv=["streamlit", "run", "espnet_tts_app_streamlit.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    streamlit_run()
