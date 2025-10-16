from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="student-performance-predictor",
    version="0.1.0",
    author="John Wesly",
    author_email="your.email@example.com",  # Update with your actual email
    description="A machine learning project to predict student performance based on academic and demographic factors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnwesly08/student-performance-predictor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "pre-commit>=3.0",
        ],
        "docs": [
            "mkdocs>=1.0",
            "mkdocs-material>=9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "student-predictor=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "student_predictor": ["data/*.csv", "models/*.pkl", "config/*.json"],
    },
    keywords=[
        "machine-learning",
        "education",
        "student-performance",
        "prediction",
        "data-science"
    ],
    project_urls={
        "Bug Reports": "https://github.com/johnwesly08/student-performance-predictor/issues",
        "Source": "https://github.com/johnwesly08/student-performance-predictor",
        "Documentation": "https://github.com/johnwesly08/student-performance-predictor#readme",
    },
)