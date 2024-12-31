from distutils.core import setup
import py2exe

setup(console=['bmi_calculator.py'])

***
from distutils.core import setup
import py2exe
from win32com.shell import shell

setup(
    windows=[{'script': 'bmi_calculator.py', 'icon_resources': [(1, "C:\\Users\\User\\Documents\\GitHub\\BMI-Calculator\\my_icon.ico")]}],
    options={'py2exe': {'bundle_files': 1}} 
)
***
