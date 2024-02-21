from setuptools import setup, find_packages

setup(
    name='shapes',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='shapes package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Leooruko/shapes',
    author='Leon Oruko', 
    author_email='orukoleon94@gmail.com'
)

# python setup.py sdist bdist_wheel --universal 