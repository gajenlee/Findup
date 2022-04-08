from cx_Freeze import setup, Executable

from packges.importer.importer import *
from packges.app.uis.access import ui_access
from packges.app.uis.backup import ui_backup
from packges.app.uis.create import ui_create
from packges.app.uis.login import ui_login
from packges.app.uis.main import ui_main
from packges.active.activer import *
from packges.store.store import *

# ADD FILES/FOLDERS
files = ['findupnew.ico', 'packges/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="findupnew.ico"
)

# SETUP CX FREEZE
setup(
    name="Findup",
    version="4.1.0",
    description="Store The Sudents and Teacher Data And Show",
    author="Gajen Lee Network",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
