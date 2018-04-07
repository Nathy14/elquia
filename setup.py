from setuptools import setup


setup(
    name="elquia",
    version="0.1",
    description="Elquia text rpg",
    url="https://github.com/Nathy14/elquia",
    author="Edison Neto",
    author_email="ednetoali@gmail.com",
    license="GPLv2",
    packages=['elquia'],
    install_requires=['pygame'],
    include_data_package=True,
    zip_safe=False
)
