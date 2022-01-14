from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A Python wrapper around the Pushbullet API.'
LONG_DESCRIPTION = 'A Python wrapper for the Pushbullet API to send different types of push notifications to your phone or/and computer.'

# Setting up
setup(name="pushbullet-python",
      version=VERSION,
      author="Janu Lingeswaran",
      author_email="<janu@lingeswaran.com>",
      description=DESCRIPTION,
      url = "https://github.com/EinGuterWaran/pushbullet-python",
      long_description_content_type="text/markdown",
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=['requests', 'requests.structures.CaseInsensitiveDict'],
      keywords=[
          'python', 'push bullet', 'push', 'bullet', 'push notifications',
          'push notification', 'API wrapper'
      ],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ])
