from setuptools import setup , find_packages
from typing import List


def get_requirements( file_path : str) -> List[str]:

    '''
    This function returns a list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirments = []
    with open(file_path) as f:
        requirments = f.readlines()
        requirments = [r.replace('\n', '') for r in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

        return requirments



setup(
    name = "Ml_project",
    version = "0.1",
    packages = find_packages(),
    author='Ashok',
    author_email='<EMAIL>',
    description = "This is a ML project for Practice",
    autor_email = 'ashokmevada18@gmail.com',
    install_requires = get_requirements('requirments.txt')
)