from setuptools import setup
import appdirs

import ethunder

config_dir = appdirs.user_config_dir("ethunder", appauthor=None)

config = {
    'name': 'EThunder',
    'description': 'A test project.',
    'author': 'Richard Pfeifer',
    'author_email': 'rip@wgd2.de',
    'url': "http://ri-p.github.io/enlighted-thunder",
    'description': ("A project to explore the possibilities of GitHub."),
    'license': 'GNU General Public License V2 (GPLv3)',
    'long_description': "EnlightedThunder is a personal test tool to explore the possiblities of GitHub and Python deployment. Please don't expect any use.",
    'classifiers': ["Development Status :: 3 - Alpha",
                    "License :: OSI Approved :: General Public License v2",
                    "Environment :: Console",
                    "Programming Language :: Python :: 2.7",
                    "Operating System :: POSIX :: Linux",
                    ],

    'version': ethunder.__version__,
    'install_requires': ['docopt==0.6.1',
                         'appdirs==1.4.0',
                         'nose==1.3.4',
			 'pyYaml==3.11',
                         ],
    'packages': ['ethunder', 'ethunder.test'],
    'data_files': [(config_dir, ['cfg/config.yml'])],
    'include_package_data': True,
    'entry_points': {'console_scripts':
                        ['ethunder = ethunder.app:Main',
                        ]
                    },
    'scripts': ['bin/ethunder'],
    'test_suite': 'nose.collector',
}

setup(**config)
