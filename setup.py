import os
from setuptools import find_packages, setup

from admin_ip_restrictor import __version__

PROJECT_DIR = os.path.dirname(__file__)

with open(os.path.join(PROJECT_DIR, 'README.rst')) as readme:
    long_description = readme.read()

install_requires = [
    'django>=1.11,<4; python_version >= "3.6.0"',
    'django-ipware>=2,<4; python_version >= "3.6.0"',
    'django>=1.11,<3; python_version < "3.6.0"',
    'django-ipware>=2,<3; python_version < "3.6.0"'
]

test_requires = [
    'coverage==6.2',
    'pytest==6.2.5',
    'pytest-cov==3.0.0',
    'pytest-django==4.5.2',
    'pytest-sugar==0.9.4',
    'tox==3.24.4',
]

setup(
    name='django-admin-ip-restrictor',
    version=__version__,
    packages=find_packages(exclude=["tests.*", "tests", ".tox"]),
    include_package_data=True,
    license='MIT License',
    description='A Django middleware to restrict incoming IPs to admin panel',
    long_description=long_description,
    url='https://github.com/sdonk/django-admin-ip-restrictor/',
    author='Alessandro De Noia',
    author_email='alessandro.denoia@gmail.com',
    install_requires=install_requires,
    extras_require={
        'tests': test_requires,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
