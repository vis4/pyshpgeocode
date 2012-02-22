from setuptools import setup, find_packages

long_desc = """
shpgeocode is a library for reverse geocoding using ESRI shapefiles
"""


setup(
    name='pyshpgeocode',
    version='0.1',
    description="reverse geocoding using shapefiles",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Gregor Aisch',
    author_email='gregor.aisch@okfn.org',
    url='http://okfnlabs.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests','test.*']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=["pyshp"],
    tests_require=[],
    entry_points={}
)
