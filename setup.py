import setuptools

setuptools.setup(
    name='connection',
    version='2021.1.5',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
