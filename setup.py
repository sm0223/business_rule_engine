from setuptools import setup, find_packages

setup(
    name='bre',
    version='0.1.0',
    description='Project requiring pyDMNrules, flask, openpyxl, xsdata',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyDMNrules',
        'Flask',
        'openpyxl',
        'xsdata',
        'dataclass_json'
    ],
    python_requires='>=3.8',
)