from setuptools import setup, find_packages

setup(
    name='halo-tea',
    version='0.1.0',
    author='cefiyana1',
    description='Package Python dari proyek halo-tea',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'halo-tea=main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
