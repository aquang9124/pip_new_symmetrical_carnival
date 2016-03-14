
import re
from setuptools import setup, find_packages


version = re.search(
   '^__version__\s*=\s*"(.*)"',
   open('pip_demo/pip_demo.py').read(),re.M).group(1)


with open("README.rst", "rb") as f:
   long_descr = f.read().decode("utf-8")


setup(
   name = "pip_demo",
   packages = find_packages(),
   entry_points = {
       "console_scripts": ['pip_demo = pip_demo.pip_demo:awesome_module']
       },
   version = version,
   description = "Python command line html creator",
   long_description = long_descr,
   author = "Alex Quang",
   author_email = "im.alex.quang@gmail.com",
   url = "https://github.com/oscarvazquez/command_line_tool_demo"
)