from setuptools import setup, find_packages

#
def get_install_requires(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    return [x.strip() for x in lines]

setup(
    name="KLineMACDSum", 
    version='0.0.2',
    author="WEN",
    description='Statistic of MACD sum of a specified period.',
    long_description='https://github.com/GoodManWEN/KLineMACDSum',
    long_description_content_type="text/markdown",
    url="https://github.com/GoodManWEN/KLineMACDSum",
    packages = find_packages(),
    install_requires = get_install_requires('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Framework :: AsyncIO',
    ],
    python_requires='>=3.7',
    keywords=["aiohttp" , "stock", "MACD"],
    include_package_data=True,
)                                                         
