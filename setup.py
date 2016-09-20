import setuptools

from cdnjspm import __VERSION_STR__

setuptools.setup(
    name='cdnjspm',
    version=__VERSION_STR__,
    description=(
        'cdnjs package manager'
    ),
    author='wushuyi',
    author_email='wushuyi541@gmail.com',
    url='http://github.com/wushuyi',
    package_dir={'cdnjspm': 'cdnjspm'},
    packages=['cdnjspm'],
    install_requires=open('requirements.txt').read().splitlines(),
    license='MIT License',
    zip_safe=False,
    keywords='cdnjs package manager',
    classifiers=[],
    entry_points={
        'console_scripts': [
            'cdnjspm = cdnjspm.main:cli'
        ]
    }
)
