#!/usr/bin/env python

from distutils.core import setup

setup(name="dronebl-tools",
      version="0.3",
      description="Tools for accessing DroneBL.",
      author="William Pitcock",
      author_email="nenolod@dereferenced.org",
      url="https://dronebl.org/",
      py_modules=['DroneBLClient'],
      scripts=['dronebl-submit', 'dronebl-query']
)
