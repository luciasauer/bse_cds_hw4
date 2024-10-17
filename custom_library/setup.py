from setuptools import setup, find_packages

setup(
    name='diabetes_detector',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'scikit-learn'
    ],
    author='Lucia Sauer, Julian Romero',
    author_email='lucia.sauer@bse.eu, julian.romero@bse.eu',
    description='Una breve descripción de tu paquete.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://www.bse.eu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
