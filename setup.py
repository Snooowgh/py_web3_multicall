import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'web3_multicall'

setuptools.setup(
    name='web3_multicall',
    version='0.0.7',
    author='Kristóf-Attila Kovács',
    description='web3_multicall',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Snooowgh/py_web3_multicall',
    packages=setuptools.find_packages(),
    install_requires=[
        'eth-abi>=4.2.1',
        'eth-utils>=2.2.1',
        'jsoncodable>=0.1.7',
        'web3>=6.9.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)
