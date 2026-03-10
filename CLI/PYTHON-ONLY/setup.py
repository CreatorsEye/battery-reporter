from setuptools import setup, find_packages

setup(
    name="cebt",
    version="1.0.0",
    description="Creators Eye Battery Tester - CLI version",
    author="Creators Eye Team",
    author_email="Creatorseye@gmail.com",
    py_modules=["cebt"],
    entry_points={
        "console_scripts": [
            "cebt=cebt:main",
        ],
    },
    install_requires=[
        "psutil>=5.8.0",
        "matplotlib>=3.5.0",
    ],
    python_requires=">=3.6",
    url="https://github.com/CreatorsEye/battery-reporter",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
