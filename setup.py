from cx_Freeze import setup, Executable

executables = [Executable('main.py',targetName='PDF_Header_Changer.exe', base='Win32GUI', icon='Unibelus_ico.ico')]



excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar', 'functools',
            'weakref', 'tokenize', 'base64', 'gettext', 'heapq', 're', 'operator',
            'bz2', 'fnmatch', 'getopt', 'reprlib', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'keyword', 'linecache']

options = {
    'build_exe': {
        'include_msvcr': True,
        'include_files': ["FreeSans.ttf", "Unibelus_ico.ico", "Unibelus_logo.png"]
    }
}

setup(name='Редактор атрибутов PDF-Файлов для сайта Unibelus',
      version='0.0.1',
      description='Редактор атрибутов PDF-Файлов для сайта Unibelus',
      executables=executables,
      options=options)