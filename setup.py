from setuptools import setup, find_packages

setup(
    name="halo-tea",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'halo-tea = main:say_hello',  # This links to your main.py function
        ],
    },
)
