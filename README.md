MCServerLib
===========

MCServerLib is a Python library that helps build Minecraft servers.

# Installation

### From PyPi:

`pip install MCServerLib`


### From Repo:

`python -m pip install git+https://github.com/myoung2namur/MCServerLib`

# Usage

```py
import MCServerLib as mcs

properties = mcs.Prop.Properties()
properties.properties['enable-command-block'] = 'true'

setup = mcs.Setup.Setup(version='1.16.5',xmx='1024M',xms='3G',properties=properties)

# Setup Server Files

# Download All Basic Server Files
setup.downloadAll() 

# Download Only Paper Bukkit
setup.downloadPaper()

# Make Only Batch File
setup.makeBatch()

# Make only Eula File
setup.makeEula()