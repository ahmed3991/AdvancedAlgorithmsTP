from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="complexity",
    version="1.0.0",
    packages=find_packages(),
    description="Description of your library",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
