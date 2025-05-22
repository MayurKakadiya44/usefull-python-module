# --- Introduction to the Setuptools Module ---
# The `setuptools` module is a standard library extension for packaging and distributing Python projects.
# It simplifies the process of creating, building, and installing Python packages, making it easier to share code.
# Core features:
# - Defines package metadata (name, version, author, etc.) in a `setup.py` or `pyproject.toml` file.
# - Manages dependencies and their versions.
# - Supports building source distributions (`sdist`) and wheel distributions (`wheel`).
# - Facilitates package installation via `pip` and uploading to PyPI.
# - Provides entry points for command-line scripts and package discovery.
# - Requires installation: `pip install setuptools`.

# Note: This script simulates a package setup in a single file for demonstration.
# In practice, you would organize code in a project directory with a `setup.py` or `pyproject.toml` file.
# We'll create a simple package, build it, and demonstrate key setuptools features.

import setuptools
import os
import shutil
from setuptools import setup, find_packages

# --- 1. Setting Up a Sample Package Structure ---
print("--- Creating Sample Package Structure ---")
# Create a temporary directory for the demo package
os.makedirs("my_package", exist_ok=True)

# Create a simple module file: my_package/__init__.py
with open("my_package/__init__.py", "w") as f:
    f.write('__version__ = "1.0.0"\n')

# Create a module with a function: my_package/utils.py
os.makedirs("my_package/submodule", exist_ok=True)
with open("my_package/submodule/utils.py", "w") as f:
    f.write('def greet(name):\n    return f"Hello, {name}!"\n')

# Create a script for entry point: my_package/scripts/cli.py
os.makedirs("my_package/scripts", exist_ok=True)
with open("my_package/scripts/cli.py", "w") as f:
    f.write('def main():\n    print("Running CLI script!")\n')

print("Sample package structure created: my_package/")

# --- 2. Creating a setup.py File ---
print("\n--- Creating setup.py ---")
# Normally, this would be a separate `setup.py` file in the project root.
# For this demo, we define it inline and write it to a file.
setup_script = """
from setuptools import setup, find_packages

setup(
    name="my-package",
    version="1.0.0",
    author="MayurKakadiya",
    author_email="kakadiya.mayur44@gmail.com",
    description="A sample Python package for demonstration",
    long_description=open('README.md').read() if os.path.exists('README.md') else "A simple package",
    long_description_content_type="text/markdown",
    url="https://github.com/example/my-package",
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],  # Example dependency
    entry_points={
        'console_scripts': [
            'my-cli=my_package.scripts.cli:main',  # CLI script entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
"""

# Write setup.py to disk
with open("setup.py", "w") as f:
    f.write(setup_script)
print("setup.py created")

# Create a basic README.md for long_description
with open("README.md", "w") as f:
    f.write("# My Package\nA simple Python package for learning setuptools.")
print("README.md created")

# --- 3. Finding Packages Automatically ---
print("\n--- Finding Packages ---")
# `find_packages()` discovers all packages in the project directory
packages = find_packages()
print("Discovered packages:", packages)  # Output: ['my_package', 'my_package.submodule', 'my_package.scripts']

# --- 4. Building a Source Distribution ---
print("\n--- Building Source Distribution ---")
# Simulate running: python setup.py sdist
# This creates a .tar.gz file in dist/
try:
    from setuptools.command.sdist import sdist
    import subprocess
    subprocess.run(["python", "setup.py", "sdist"], check=True)
    print("Source distribution created in dist/")
except subprocess.CalledProcessError as e:
    print("Error building sdist:", e)

# --- 5. Building a Wheel Distribution ---
print("\n--- Building Wheel Distribution ---")
# Simulate running: python setup.py bdist_wheel
# Requires `wheel` package: pip install wheel
try:
    subprocess.run(["python", "setup.py", "bdist_wheel"], check=True)
    print("Wheel distribution created in dist/")
except subprocess.CalledProcessError as e:
    print("Error building wheel:", e)

# --- 6. Installing the Package Locally ---
print("\n--- Installing Package Locally ---")
# Simulate running: pip install .
try:
    subprocess.run(["pip", "install", "."], check=True)
    print("Package installed locally")
except subprocess.CalledProcessError as e:
    print("Error installing package:", e)

# --- 7. Testing the Installed Package ---
print("\n--- Testing Installed Package ---")
try:
    from my_package.submodule.utils import greet
    print("Calling greet function:", greet("Alice"))  # Output: Hello, Alice!
except ImportError as e:
    print("Error importing package:", e)

# --- 8. Testing the Entry Point (CLI Script) ---
print("\n--- Testing CLI Entry Point ---")
# Simulate running the CLI script: my-cli
try:
    subprocess.run(["my-cli"], check=True)
    print("CLI script executed successfully")
except subprocess.CalledProcessError as e:
    print("Error running CLI script:", e)

# --- 9. Specifying Dependencies ---
print("\n--- Dependency Management ---")
# Dependencies are specified in `install_requires` in setup.py
# Example: 'requests>=2.25.1' ensures the package is installed with the dependency
print("Dependencies defined in setup.py: ['requests>=2.25.1']")

# --- 10. Using Classifiers for Metadata ---
print("\n--- Using Classifiers ---")
# Classifiers in setup.py provide metadata for PyPI (e.g., Python version, license)
print("Example classifiers defined: Python 3, MIT License, OS Independent")

# --- 11. Error Handling and Edge Cases ---
print("\n--- Error Handling ---")
# Handle missing files (e.g., README.md)
try:
    with open("nonexistent.md", "r") as f:
        pass
except FileNotFoundError as e:
    print("Error: Missing file:", e)

# Handle invalid package names
try:
    setup(name="invalid@package", version="1.0")  # Invalid package name
except ValueError as e:
    print("Error: Invalid package name:", e)

# --- 12. Cleaning Up ---
print("\n--- Cleaning Up ---")
# Remove temporary files and directories
try:
    shutil.rmtree("my_package")
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("my_package.egg-info", ignore_errors=True)
    os.remove("setup.py")
    os.remove("README.md")
    print("Temporary files and directories removed")
except OSError as e:
    print("Error during cleanup:", e)

# --- 13. Note on Uploading to PyPI ---
print("\n--- Note on PyPI Upload ---")
# To upload to PyPI, use: twine upload dist/*
# Requires `twine` package: pip install twine
# Example: twine upload dist/my-package-1.0.0.tar.gz
print("To upload to PyPI, install twine and run: twine upload dist/*")
