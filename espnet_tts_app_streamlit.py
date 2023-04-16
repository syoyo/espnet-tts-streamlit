import io
import time
import base64
import soundfile

import numpy as np
import streamlit as st
import torch
import soundfile as sf
import matplotlib.pyplot as plt 

from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none


def st_autoplay_audio(st, audio_bytes, sample_rate):
    """
    audio_bytes : np.ndarray dtype fp32
    """

    buf = io.BytesIO()
    soundfile.write(buf, audio_bytes, samplerate=sample_rate, format='WAV')

    wavdata = buf.getvalue()
    
    # https://github.com/streamlit/streamlit/issues/2446#issuecomment-1465017176
    audio_base64 = base64.b64encode(wavdata).decode('utf-8')
    audio_tag = f'<audio autoplay="true" src="data:audio/wav;base64,{audio_base64}">'
    st.markdown(audio_tag, unsafe_allow_html=True)

def init_session_state(st, key, value):
    if key not in st.session_state:
        st.session_state[key] = value

def get_state(st, key):
    if key not in st.session_state:
        st.error("Internal error: `{}` not present in session_state.".format(key))

    return st.session_state.get(key)

init_session_state(st, "lang", 'Japanese')
init_session_state(st, "tag", 'kan-bayashi/tsukuyomi_full_band_vits_prosody')
init_session_state(st, "vocoder_tag", 'none')
init_session_state(st, "device", 'cpu')
init_session_state(st, "text2speech", None)
init_session_state(st, "model_loaded", False)
#init_session_state(st, "wavdata", None)

st.title("ESPnet2 TTS")

#lang = 'Japanese'
#tag = 'kan-bayashi/jsut_full_band_vits_prosody'
#vocoder_tag = 'none'

def init_tts_model(tag, vocoder_tag, device, speed_control_alpha=1.0, noise_scale=0.333, noise_scale_duration=0.333):
    text2speech = Text2Speech.from_pretrained(
        model_tag=str_or_none(tag),
        vocoder_tag=str_or_none(vocoder_tag),
        device=device,
        # Only for Tacotron 2 & Transformer
        threshold=0.5,
        # Only for Tacotron 2
        minlenratio=0.0,
        maxlenratio=10.0,
        use_att_constraint=False,
        backward_window=1,
        forward_window=3,
        # Only for FastSpeech & FastSpeech2 & VITS
        speed_control_alpha=speed_control_alpha,
        # Only for VITS
        noise_scale=noise_scale,
        noise_scale_dur=noise_scale_duration,
    )

    return text2speech

# TODO: "Mandarin", "English"
lang = st.selectbox("Language", options=["Japanese"])

st.header("Tsukuyomi-chan + JUST audio data terms-of-use info")
st.markdown("https://tyc.rei-yumesaki.net/material/corpus/")
st.markdown("https://sites.google.com/site/shinnosuketakamichi/publication/jsut/")

agreed = st.checkbox("Agree the terms of use of Tukuyomi-chan copus + JUST copus dataset", value=False)

tag = st.selectbox("Model", options=["kan-bayashi/tsukuyomi_full_band_vits_prosody"])

speed_control_alpha = st.number_input("Speed", value=1.0, min_value=0.1, max_value=3.0, help="Speech speed. Larger value become slow")
#noise_scale = st.number_input("Noise scale", value=0.333, min_value=0.0, max_value=1.0)
#noise_scale_duration = st.number_input("Noise scale duration", value=0.333, min_value=0.0, max_value=1.0)


if st.button("Load/Setup model", disabled=not agreed, help="This may take 20~30 mins for the first time to download the pretrained model(See console output for details)."):
    tag = get_state(st, "tag")
    vocoder_tag = get_state(st, "vocoder_tag")
    device = get_state(st, "device")

    with st.spinner("Loading and setting up TTS model...(this may take 20~30 mins for the first time. Be patient...)"):

        text2speech = init_tts_model(tag, vocoder_tag, device, speed_control_alpha=speed_control_alpha)

        st.session_state["text2speech"] = text2speech

        # delete previous audio data.
        if 'wavdata' in st.session_state:
            del st.session_state['wavdata']

text = st.text_area("Text", value="吾輩は猫である。名前はまだない。", max_chars=2048)

autoplay_onoff = st.checkbox("Auto play")

model_not_loaded = st.session_state['text2speech'] is None

if st.button("Synth!", disabled=model_not_loaded):
    module = st.session_state["text2speech"]

    with torch.no_grad():
        ts = module(text)["wav"]

        wavdata = ts.view(-1).cpu().numpy()

        st.session_state["wavdata"] = wavdata


if "wavdata" in st.session_state:
    wavdata = get_state(st, 'wavdata')
    samplerate = st.session_state["text2speech"].fs
    st.audio(wavdata, sample_rate=samplerate)

    if autoplay_onoff is True:
        st_autoplay_audio(st, wavdata, samplerate)

    with st.expander("Waveform visualization"):
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.plot(wavdata)

        ax2 = fig.add_subplot(2, 1, 2)
        ax2.specgram(wavdata, Fs=samplerate)
        
        st.pyplot(fig)

st.warning("How to quit app? Please first ctrl-c(several times may be required) Streamlit process in terminal window, then close a browser window.")
