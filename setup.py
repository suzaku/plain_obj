from distutils.core import setup

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='plain_obj',
    version='0.1.1',
    description='A faster alternative to namedtuple.',
    long_description=long_description,
    url='https://github.com/suzaku/plain_obj',
    license='MIT',
    author='Satoru Logic',
    author_email='satorulogic@gmail.com',
    py_modules=['plain_obj'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tuple',
)
