from setuptools import find_packages, setup
from typing import List


DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if DOT_E in requirements:
            requirements.remove(DOT_E)

    return requirements

setup(
name ="mlproject",
version="0.0.1",
author="Rohan",
author_email="ronapradhan68@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)



