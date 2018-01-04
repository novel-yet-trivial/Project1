# -*- mode: python -*-

block_cipher = None

added_files = [
         ( "bcgr.png", '.'), 
         ( "my_icon.ico", '.'),                            
         ]


a = Analysis(['Newnew.py'],
             pathex=['D:\\My Project'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Newnew',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='D:\\My Project\\my_icon.ico')
