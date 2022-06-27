from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9'
]

requires = [
    'certifi',
    'chardet',
    'idna',
    'requests',
    'urllib3'
]

setup(
    name='PSNAWP',
    version='2021.20.6',
    packages=find_packages(),
    install_requires=requires,
    project_urls={
        "Change Log": "https://github.com/tflecht/psnawp/commits/",
        "Documentation": "https://psnawp.readthedocs.io/en/latest/",
        "Issue Tracker": "https://github.com/tflecht/psnawp/issues",
        "Source Code": "https://github.com/tflecht/psnawp",
    },
    url='https://github.com/tflecht/psnawp',
    license='MIT',
    author='isFakeAccount',
    author_email='trevorphillips@gmx.us',
    description='Retrieve User Information, Trophies, Game and Store data from the PlayStation Network',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='PSN API',
    classifiers=classifiers
)
