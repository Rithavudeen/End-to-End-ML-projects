from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace() for req in requirements ]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(name="ML_project",version="0.0.1",author="Mohamed rithavudeen",author_email="mdrithavudeen20@gamil.com",
      packages=find_packages(),install_requires=get_requirements("requirements.txt"))