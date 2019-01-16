import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='globber',
    version='0.2.0',
    author='Jaakko Kangasharju',
    author_email='ashar@iki.fi',
    description='Library for string matching with glob patterns',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/asharov/globber',
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent'
    ]
)
