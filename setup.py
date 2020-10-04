from setuptools import find_packages, setup

setup(
    name=’cryptoLibrary’,
    packages=find_packages(include=[‘cryptoLibrary’]),
    version=’0.1.0',
    description=’A Python Cryptography Library’,
    author=’Me’,
    license=’MIT’,
    install_requires=[],
    setup_requires=[‘pytest-runner’],
    tests_require=[‘pytest==4.4.1’],
    test_suite=’tests’
)
