from setuptools import setup, find_packages

setup(
    name="halo-tea",
    version="0.1",
    author="cefiyana1",
    description="Package Python dari proyek halo-tea",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "halo-tea = halo_tea.main:say_hello",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
