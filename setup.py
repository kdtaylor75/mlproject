from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(filepath: str) -> list[str]:
    """
    This function returns the list of requirements provided in requirements.txt.
    """
    requirements = []

    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Kris Taylor",
    author_email="kdtaylor75@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
