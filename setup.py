from setuptools import setup, find_packages

setup(
    name='aes-keywrap',
    version='17.12.0',
    url='https://github.com/kurtbrose/aes_keywrap',
    author='Kurt Rose',
    author_email='kurt@kurtrose.com',
    decription="aes keywrap (RFC 3394 + RFC 5649)",
    long_description = open('README.rst').read(),
    py_modules=['aes_keywrap'],
)
