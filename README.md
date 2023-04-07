# Requirements

- Python 3.8(Python 3.10+ may not work)
- PyTorch
  - We use CPU version for portability.

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

espnet-tts-streamlit is licensed under MIT license.

### Third party licenses

- Streamlit: Apache 2.0
- ESPNet, ESPNet2: Apache 2.0
- Other python packages/modules: See license of each Python packages/modules
  - Short summary: May contain package/module in GPL or GPL like licenses, but no package/module which cannot be used in non-commercial.

### Pretrained model licenses

- T.B.W.
