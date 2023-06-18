from setuptools import find_packages, setup

setup(
    name="el_meltano",
    packages=find_packages(exclude=["el_meltano_tests"]),
    install_requires=[
    "dagster",
    "dagster-meltano"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
