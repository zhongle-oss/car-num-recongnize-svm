# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mian.py','/Users/zhongle/Downloads/车牌识别/Recognition.py','/Users/zhongle/Downloads/车牌识别/Demo_投影法.py','/Users/zhongle/Downloads/车牌识别/json文件创建 .py'],
             pathex=['/Users/zhongle/Downloads/车牌识别'],
             binaries=[],
             datas=[('/Users/zhongle/Downloads/车牌识别/cardtype.json','cardtype.json'),
             ('/Users/zhongle/Downloads/车牌识别/Prefecture.json','Prefecture.json'),
             ('/Users/zhongle/Downloads/车牌识别/provinces.json','provinces.json'),
             ('/Users/zhongle/Downloads/车牌识别/svm.dat','svm.dat'),
             ('/Users/zhongle/Downloads/车牌识别/svmchinese.dat','svmchinese.dat')],
             hiddenimports=[],
             hookspath=[],
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
          name='mian',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mian')
