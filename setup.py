#!/usr/bin/env python

## NOTE: ##
## this setup.py was generated by zero2pypi:
## http://gfxmonk.net/dist/0install/zero2pypi.xml

from setuptools import *
setup(
	packages = find_packages(exclude=['test', 'test.*']),
	description='coloured output for nosetests',
	entry_points={'nose.plugins.0.10': ['NOSETESTS_PLUGINS = rednose:RedNose']},
	install_requires=['setuptools', 'python-termstyle >=0.1.7'],
	long_description="\n**Note**: This package has been built automatically by\n`zero2pypi <http://gfxmonk.net/dist/0install/zero2pypi.xml>`_.\nIf possible, you should use the zero-install feed instead:\nhttp://gfxmonk.net/dist/0install/rednose.xml\n\n----------------\n\n=========\nrednose\n=========\n\nrednose is a `nosetests`_\nplugin for adding colour (and readability) to nosetest console results.\n\nInstallation:\n-------------\n::\n\n\teasy_install rednose\n\t\nor from the source::\n\n\t./setup.py develop\n\nUsage:\n------\n::\n\n\tnosetests --rednose\n\nor::\n\n\texport NOSE_REDNOSE=1\n\tnosetests\n\nRednose by default uses auto-colouring, which will only use\ncolour if you're running it on a terminal (i.e not piping it\nto a file). To control colouring, use one of::\n\n\tnosetests --rednose --force-color\n\tnosetests --no-color\n\n(you can also control this by setting the environment variable NOSE_REDNOSE_COLOR to 'force' or 'no')\n\n.. _nosetests: http://somethingaboutorange.com/mrl/projects/nose/\n",
	name='rednose',
	py_modules=['rednose'],
	url='http://gfxmonk.net/dist/0install/rednose.xml',
	version='0.4.0',
classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Software Development :: Testing",
	],
	keywords='test nosetests nose nosetest output colour console',
	license='BSD',
)
