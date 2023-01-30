from setuptools import setup, find_packages

setup(
    name='ohlc-bot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'os',
        'requests',
        'pandas',
        'arrow',
        'xlrd',
        'pymysql',
        'sqlalchemy',
        'datetime',
        'threading'
        'venv'
    ],
    entry_points={
        'console_scripts': [
            'mypackage=mypackage.__main__:main'
        ]
    },
)