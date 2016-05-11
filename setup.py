import io
import os

from setuptools import setup, find_packages
from fftool import __version__


here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.rst'), encoding='utf8') as f:
    README = f.read()

with io.open(os.path.join(here, 'requirements.txt'), encoding='utf8') as f:
    REQS = f.read().splitlines()


extra_options = {
    'packages': find_packages(),
}


setup(name='ff-tool',
      version=__version__,
      description='Firefox browser CLI test setup tool',
      long_description=README,
      classifiers=['Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7'
                   ],
      keywords='[firefox, test, pref, profile, download, install]',
      author='Johnny Quest',
      author_email='cloud-services-qa@mozilla.org',
      license='MPL2',
      install_requires=REQS,
      package_data={'fftool': ['configs/*.ini']},
      include_package_data=True,
      zip_safe=False,
      entry_points='''
      [console_scripts]
      ff = fftool.main:main
      ''',
      **extra_options
      )
