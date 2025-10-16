Here's the `CONTRIBUTING.md` file:

```markdown
# Contributing to Student Performance Prediction Project

Thank you for your interest in contributing to the Student Performance Prediction project! We welcome contributions from the community and are grateful for your help in making this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Exercise consideration and respect in your speech and actions
- Attempt collaboration before conflict
- Refrain from demeaning, discriminatory, or harassing behavior

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your forked repository**
   ```bash
   git clone https://github.com/johnwesly08/student-performance-predictor.git
   cd student-performance-predictor
   ```

3. **Add the original repository as upstream**
   ```bash
   git remote add upstream https://github.com/johnwesly08/student-performance-predictor.git
   ```

## Development Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install development dependencies
   ```

3. **Set up pre-commit hooks** (recommended)
   ```bash
   pre-commit install
   ```

## Making Changes

1. **Sync your fork** with the upstream repository
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a new branch** for your feature or fix
   ```bash
   git checkout -b feature/your-feature-name
   # or for bug fixes:
   git checkout -b fix/issue-description
   ```

3. **Make your changes** following the code style guidelines

4. **Test your changes**
   ```bash
   pytest tests/ -v
   ```

5. **Commit your changes** using conventional commit messages
   ```bash
   git add .
   git commit -m "feat: add new prediction endpoint"
   ```

### Conventional Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semi-colons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks, dependency updates

## Pull Request Process

1. **Push your changes** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** from your fork to the main repository

3. **Fill out the PR template** with:
   - Description of changes
   - Related issue number (if applicable)
   - Testing performed
   - Screenshots (if UI changes)

4. **Wait for review** and address any feedback

5. **Once approved**, your PR will be merged

## Reporting Bugs

When reporting bugs, please include:

### Bug Report Template
```markdown
## Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Windows, macOS, Linux]
- Python Version: [e.g., 3.8, 3.9]
- Package Version: [e.g., 0.1.0]

## Additional Context
Any other context about the problem.
```

## Suggesting Features

We welcome feature suggestions! Please use this template:

### Feature Request Template
```markdown
## Problem Statement
A clear and concise description of the problem you're trying to solve.

## Proposed Solution
A clear and concise description of what you want to happen.

## Alternatives Considered
A clear and concise description of any alternative solutions or features you've considered.

## Additional Context
Add any other context or screenshots about the feature request here.
```

## Code Style Guidelines

### Python Code Style
- Follow [PEP 8](https://pep8.org/) guidelines
- Use type hints for all function parameters and return values
- Maximum line length: 88 characters (enforced by Black)
- Use descriptive variable and function names

### Docstring Format (Google Style)
```python
def predict_student_performance(data: pd.DataFrame) -> np.ndarray:
    """Predict student performance based on input features.

    Args:
        data: DataFrame containing student features with columns:
            - 'age': Student age
            - 'grades': Previous grades
            - 'attendance': Attendance percentage

    Returns:
        numpy.ndarray: Array of predicted performance scores

    Raises:
        ValueError: If required columns are missing from input data
    """
```

### Import Organization
```python
# Standard library imports
import os
import sys
from typing import Dict, List

# Third-party imports
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Local imports
from src.data_loader import load_student_data
from src.preprocessing import clean_data
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_model.py -v

# Run tests with specific marker
pytest -m "slow"  # Run slow tests
```

### Writing Tests
- Place test files in the `tests/` directory
- Use descriptive test method names
- Test both expected behavior and edge cases
- Mock external dependencies when appropriate

## Questions?

If you have any questions about contributing, please:
1. Check the existing documentation
2. Search existing issues
3. Open a new issue with the "question" label

## Recognition

All contributors will be recognized in our README.md and release notes. We appreciate every contribution, no matter how small!

---

Thank you for contributing to the Student Performance Prediction project! 🎓
```