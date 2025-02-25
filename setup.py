"""
The setup.py file is essential part of packaging and 
distributing python projects. It is used by setuptools
To define the configuration of your projects,
such as its metadata,dependencies and more 
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e . 
                # -e . is respnsible for refering the setup file
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="satyasai",
    author_email="satyasai.ch10@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
                
            
        