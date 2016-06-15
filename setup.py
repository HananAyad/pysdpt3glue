""" sdpt3glue package information.
"""
from setuptools import setup, find_packages


def _load_requires_from_file(filepath):
    """ Read a package list from a given file path.

    Args:
      filepath: file path of the package list.

    Returns:
      a list of package names.
    """
    with open(filepath) as fp:
        return [pkg_name.strip() for pkg_name in fp.readlines()]


setup(
    name = 'py-sdpt3-glue',
    version = '0.1.0',
    description=(
        'Glue code for solving semidefinite programs '
        'in Cvxpy format using the SDPT3 package for Matlab.'
    ),
    author="Trish Gillett-Kawamoto",
    url="https://github.com/discardthree/PySDPT3glue",
    packages = find_packages(exclude=["tests"]),
    install_requires=_load_requires_from_file("requirements.txt"),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    test_suite = 'tests.suite',
    license="MIT"
)