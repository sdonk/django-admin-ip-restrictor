import os
from setuptools import find_packages, setup

from admin_ip_restrictor import __version__

PROJECT_DIR = os.path.dirname(__file__)

with open(os.path.join(PROJECT_DIR, 'README.rst')) as readme:
    long_description = readme.read()

install_requires = [
    'django>=1.11,<3',
    'django-ipware>=2,<3'
]

test_requires = [
    'coverage==5.0.2',
    'pytest==5.3.2',
    'pytest-cov==2.8.1',
    'pytest-django==3.7.0',
    'pytest-sugar==0.9.2',
    'tox==3.14.3',
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
