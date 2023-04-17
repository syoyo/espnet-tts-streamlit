import io
import streamlit as st

import librosa

from faster_whisper import WhisperModel

st.title("Whisper ASR UI")

model_size = "large-v2"
device="cpu"

compute_type = "float16"
if device == "cpu":
    # Use fp32 since fp16 is not efficiently supported on most CPU architectures. 
    compute_type = "float32"

if st.button("Load model."):
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    st.session_state['model'] = model

def do_transcribe(model, filename, beam_size=5):

    with st.spinner("Processing..."):
        segments, info = model.transcribe(filename, beam_size=5)

        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

            st.write(segment.text)

uploaded_file = st.file_uploader("Upload audio file.")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    buf = io.BytesIO(bytes_data)

    #do_transcribe(buf)

    st.session_state['audio_file'] = buf

beam_size = st.slider('Accuracy', value=5, min_value=1, max_value=10, help='Less value makes transcribe faster, but loose an accuracy.')

transcribe_ready = False
if 'model' in st.session_state:
    if 'audio_file' in st.session_state:
        transcribe_ready = True

if st.button("Transcribe!", disabled=not transcribe_ready):
    model = st.session_state['model']
    audio_file = st.session_state['audio_file']

    do_transcribe(model, audio_file, beam_size)
