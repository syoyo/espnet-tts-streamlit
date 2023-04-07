# -*- mode: python ; coding: utf-8 -*-

import site
import os

block_cipher = None

# Choose path containing "site-packages"
package_path = site.getsitepackages()[0]

for p in site.getsitepackages():
    if "site-package" in p:
        package_path = p
        break

# streamlit files
streamlit_datas=[(os.path.join(package_path, "altair/vegalite/v4/schema/vega-lite-schema.json"),
        "./altair/vegalite/v4/schema/"),
       (os.path.join(package_path, "streamlit/static"),"./streamlit/static"),
       (os.path.join(package_path, "streamlit/runtime"),"./streamlit/runtime"),
       ]

# app files.
app_datas = [
    ("espnet_tts_app_streamlit.py", "."),
    ("pages/*.py", "pages")
]

## other asset files
asset_datas = [
  ]

a = Analysis(
    ['espnet_tts_app.py'],
    pathex=[],
    binaries=[],
    # copy streamlit files
    datas=streamlit_datas+app_datas+asset_datas,
    hiddenimports=[],
    hookspath=["./hooks"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='espnet_tts_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='espnet_tts_app',
)
