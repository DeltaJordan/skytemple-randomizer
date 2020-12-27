# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import PurePosixPath, Path

pkg_path = os.path.abspath(os.path.join('..', 'skytemple_randomizer'))
site_packages = next(p for p in sys.path if 'site-packages' in p)

additional_files = []
additional_datas = [
    # XXX: No better way to do this? :(
    (os.path.join(pkg_path, 'data'), '/skytemple_randomizer/data'),
    (os.path.join(pkg_path, 'data'), '/data'),
    (os.path.join(pkg_path, '*.glade'), '.'),
    (os.path.join(site_packages, 'skytemple_icons', 'hicolor'), 'skytemple_icons/hicolor'),
    (os.path.join(site_packages, 'skytemple_files', '_resources'), 'skytemple_files/_resources'),
    (os.path.join('.', 'armips.exe'), 'skytemple_files/_resources'),

    # These aren't auto dectected for some reason :(
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'fontconfig'), 'share/fontconfig'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'glib-2.0'), 'share/glib-2.0'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'gtksourceview-3.0'), 'share/gtksourceview-3.0'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'icons'), 'share/icons'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'locale'), 'share/locale'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", 'share', 'themes'), 'share/themes'),

    # Themes
    ('Arc', 'share/themes/Arc'),
    ('Arc-Dark', 'share/themes/Arc-Dark')
]

additional_binaries = [
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", "bin", "libcrypto-1_1-x64.dll"), '.'),
    (os.path.join("D:/", "a", "_temp", "msys", "msys64", "mingw64", "bin", "libssl-1_1-x64.dll"), '.'),
]

block_cipher = None


a = Analysis(['../skytemple_randomizer/main.py'],
             pathex=[os.path.abspath(os.path.join('..', 'skytemple_randomizer'))],
             binaries=additional_binaries,
             datas=additional_datas,
             hiddenimports=['pkg_resources.py2_warn', 'packaging.version', 'packaging.specifiers',
                            'packaging.requirements', 'packaging.markers', '_sysconfigdata__win32_', 'win32api'],
             hookspath=[os.path.abspath(os.path.join('.', 'hooks'))],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='skytemple_randomizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon=os.path.abspath(os.path.join('.', 'skytemple_randomizer.ico')))

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               additional_files,
               strip=False,
               upx=True,
               upx_exclude=[],
               version=os.getenv('PACKAGE_VERSION', '0.0.0'),
               name='skytemple_randomizer')
