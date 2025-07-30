from setuptools import setup, find_packages

setup(
    name = 'student_marks_predictor',
    version = '1.0',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [
        'pandas','scikit-learn','joblib'
    ],
)