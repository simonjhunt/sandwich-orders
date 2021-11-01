import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='orders',
    version='0.0.1',
    author='Simon Hunt',
    author_email='simon@example.com',
    description='Adding and listing sandwich orders',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/simonjhunt/sandwich-orders',
    license='MIT',
    packages=['orders'],
    install_requires=[],
)