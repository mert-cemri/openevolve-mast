'''
Setup script for the URL shortener CLI application.
'''
from setuptools import setup, find_packages
setup(
    name='url_shortener_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'url_shortener=main:main',
            'url_shortener_gui=gui:run_gui',
        ],
    },
    author='ChatDev',
    author_email='contact@chatdev.com',
    description='A CLI tool to shorten URLs using TinyURL',
    url='https://github.com/chatdev/url_shortener_cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)