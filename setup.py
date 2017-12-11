from setuptools import setup, find_packages

setup(
    name="fin-backend",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'flask_sqlalchemy', 'envparse'],
    entry_points='''
        [console_scripts]
        feedfin=manage:cli
    '''
)
