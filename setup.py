"""The setup script."""

from setuptools import setup, find_packages
import os
import sys


def initialize_options(self):
    pass


def finalize_options(self):
    pass


def run(self):
    os.system('rm -vrf ./build ./dist ./*.pyc ./*.pyo ./*.pyd ./*.tgz ./   *.egg-info `find -type d -name __pycache__`')


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as req:
    req_list = req.readlines()
    req_list = [sd.replace('\n', '') for sd in req_list]

requirements = req_list
test_requirements = ['pytest>=3']

setup(
    author="dagmawi yohannes",
    email="dagmawi.yoh03@gmail.com",
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="A Repository structure for all project",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='Scripts',
    name='Scripts',
    packages=find_packages(include=['scripts', 'scripts.*', 'ml_analysis_practice',
                                    'data', 'dashboards', 'scripts/applications',
                                    'tests', 'notebooks', 'models']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dagmawiii03/Sales_prediciton.git',
    version='1.0.0',
    zip_safe=False,
)