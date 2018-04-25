import os
from setuptools import find_packages, setup

from admin_ip_restrictor import __version__

PROJECT_DIR = os.path.dirname(__file__)

with open(os.path.join(PROJECT_DIR, 'README.rst')) as readme:
    long_description = readme.read()

install_requires = [
    'django>=1.9,<2.1',
    'django-ipware>=2,<3'
]

test_requires = [
    'coverage==4.4.2',
    'pytest==3.2.3',
    'pytest-cov==2.5.1',
    'pytest-django==3.1.2',
    'pytest-sugar==0.9.0',
    'tox==2.9.1',
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
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
