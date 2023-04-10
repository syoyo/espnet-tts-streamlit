# ESPnet2 + TTS GUI using Streamlit

A Streamlit GUI interface for ESPnet2 + TTS(Text-to-speech). 


https://user-images.githubusercontent.com/18676/230901038-f9351513-1d68-48ca-a6a0-e1a367e5a0eb.mp4


Code is based on ESPnet2 TTS Colab demo

https://espnet.github.io/espnet/notebook/espnet2_tts_realtime_demo.html

Currently only Japanese TTS is supported.

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

## Stop the app

There is no easy way to quit/terminate Streamlit app...
(Especially on Windows)

https://discuss.streamlit.io/t/streamlit-server-1-5-1-from-command-line-hard-to-stop-with-ctrl-c/22277/2

Please first do `ctrl-c` in Terminal window to terminate streamlit process, then close the browser window.


## License

`espnet-tts-streamlit` source code is licensed under MIT license.

pretrained model and audio datasets have their own licenses and terms of use.

### Third party licenses

- Streamlit: Apache 2.0
- ESPNet, ESPNet2: Apache 2.0
- Other python packages/modules: See license of each Python packages/modules
  - Short summary: May contain package/module in GPL or GPL like licenses

### Pretrained model terms of use

- `kan-bayashi/tsukuyomi_full_band_vits_prosody`
  - `tsukuyomi_full_band_vits_prosody` model was trained using Tsukuyomi-chan copus and JUST copus(CC-BY-SA 4.0), thus you cannot use this pretrained model commercially. Use it for research purpose and personal use. DYOR.
  - https://tyc.rei-yumesaki.net/material/corpus/ 
  - https://sites.google.com/site/shinnosuketakamichi/publication/jsut/  (CC-BY-SA 4.0)

EoL.
