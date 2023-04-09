# -*- mode: python ; coding: utf-8 -*-

import site
import os
import shutil
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None


# Choose path containing "site-packages"
package_path = site.getsitepackages()[0]

for p in site.getsitepackages():
    if "site-package" in p:
        package_path = p
        break

# Overwrite librosa/__init__.py
# https://github.com/librosa/librosa/issues/1682
def librosa_postfix():
    # Check file existence
    if os.path.isfile(os.path.join(package_path, "librosa/__init__.py")):
        shutil.copyfile("pre-fix/librosa/__init__.py", os.path.join(package_path, "librosa/__init__.py"))
        print("Overwrite librosa/__init__.py")

print("Trying to patch librosa/__init__.py ...")
librosa_postfix()

# streamlit files
streamlit_datas=[(os.path.join(package_path, "altair/vegalite/v4/schema/vega-lite-schema.json"),
        "./altair/vegalite/v4/schema/"),
       (os.path.join(package_path, "streamlit/static"),"./streamlit/static"),
       (os.path.join(package_path, "streamlit/runtime"),"./streamlit/runtime"),
       ]

# app files.
app_datas = [
    ("espnet_tts_app_streamlit.py", "."),
    (os.path.join(package_path, "espnet/version.txt"), "./espnet"),
    (os.path.join(package_path, "jamo/data"), "./jamo/data"),
    # ("post-fix/librosa/__init__.pyi", "./librosa")
]

## other asset files
asset_datas = [
  ]

a = Analysis(
    ['espnet_tts_app.py'],
    pathex=[],
    binaries=[],
    # copy streamlit files
    datas=streamlit_datas+app_datas+asset_datas+collect_data_files("librosa"),
    hiddenimports=["librosa", "librosa.filters"],
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
