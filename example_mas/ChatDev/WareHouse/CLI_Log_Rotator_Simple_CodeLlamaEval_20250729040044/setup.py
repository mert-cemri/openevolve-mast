# setup.py
from setuptools import setup
setup(
    name='log_rotator',
    version='1.0',
    description='Simple CLI log rotator',
    author='ChatDev',
    author_email='support@chatdev.com',
    packages=['log_rotator'],
    install_requires=['python>=3.6'],
    entry_points={
        'console_scripts': [
            'log_rotator=log_rotator.main:main',
        ],
    },
)