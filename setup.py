from setuptools import setup, find_packages

setup(
    name="phishing-detection",
    version="0.1.0",
    description="A library for phishing detection using Hugging Face models.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo/phishing-detection",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "scikit-learn",
        "pandas",
        "numpy",
        "imblearn",
        "pyyaml",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "phishing-detection=phishing_detection.cli:main",
        ],
    },
)
