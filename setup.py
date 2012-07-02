from distribute_setup import use_setuptools
use_setuptools()

from distutils.core import setup

setup(
    name='django-pauth',
    version=".".join(map(str, __import__('pauth').__version__)),
    author="Mike O'Malley",
    author_email='spuriousdata@gmail.com',
    description='Pluggable authentication system for django.',
    long_description=open('README.rst').read(),
    license='LICENSE',
    url='http://github.com/spuriousdata/django-pauth',
    packages=['pauth'],
    include_package_data=True,
    install_requires=[
        'Django >= 1.3.0',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
