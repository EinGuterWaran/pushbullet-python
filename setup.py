from setuptools import setup, find_packages
from os import path

VERSION = '1.6.0'
DESCRIPTION = 'A Python wrapper around the Pushbullet API.'
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(name="pushbullet-python",
      version=VERSION,
      author="Janu Lingeswaran",
      author_email="<janu@lingeswaran.com>",
      description=DESCRIPTION,
      url="https://github.com/EinGuterWaran/pushbullet-python",
      long_description_content_type="text/markdown",
      long_description=LONG_DESCRIPTION,
      license='MIT License',
      packages=find_packages(),
      install_requires=['requests'],
      keywords=[
          'python', 'push bullet', 'push', 'bullet', 'push notifications',
          'push notification', 'API wrapper'
      ],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ])
