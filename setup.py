setup_args = dict(name="normws",
                  version="0.1",
                  description="normalize line breaks and remove trailing whitespace",
                  py_modules=['normws'])
try:
    from setuptools import setup, find_packages
    setup_args["entry_points"] = dict(console_scripts=["normws = normws:main"])
except ImportError:
    from distutils.core import setup

setup(**setup_args)
