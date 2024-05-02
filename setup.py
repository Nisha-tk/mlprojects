from setuptools import find_packages,setup

from typing import List


def get_requiremnets(file_path:str)->List[str]:
    #this fucntion will return the list of requiremnets
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace ("\n","") for req in requirements]
        
    return requirements        



    



setup(
name="ml Project",
version="0.0.1",
author="Nisha Tumanpelli",
author_email="nisha.333t@gmail.com",
packages=find_packages(),
install_requires=get_requiremnets("requirements.txt"),




)