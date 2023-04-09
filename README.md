# ESPNet2 + TTS GUI in Streamlit

A Streamlit GUI for ESPNet2 + TTS(Text-to-speech).
Currently only Japanese is supported.

# Requirements

- Python 3.8(Python 3.10+ did not work due to `typeguard` version used in ESPNet2))
- PyTorch
  - We use CPU version for portability
- C/C++ Build environment
  - `pyopenjtalk` requires to build from a source.

## Install

```
$ python -m pip install -r requirements.txt
```

## Run streamlit app directly

```
$ streamlit run espnet_tts_app_streamlit.py
```

## Build a Standalone exe app using pyinstaller

Install pyinstaller,

```
$ python -m pip install pyinstaller
```

Then

```
$ pyinstaller espnet-tts-app.spec
```

## License

espnet-tts-streamlit source code is licensed under MIT license.

pretrained model and audio datasets have their own licenses and terms of use.

### Third party licenses

- Streamlit: Apache 2.0
- ESPNet, ESPNet2: Apache 2.0
- Other python packages/modules: See license of each Python packages/modules
  - Short summary: May contain package/module in GPL or GPL like licenses

### Pretrained model and audio data licenses and terms of use

- https://tyc.rei-yumesaki.net/material/corpus/ 
- https://sites.google.com/site/shinnosuketakamichi/publication/jsut/ 
