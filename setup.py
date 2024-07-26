'''
we can use this to convert it into a python pacakages
'''

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirnments(file_path: str) -> List[str]:
    '''
        this function will written the list of requirnments to be downloaded.
    '''
    

    requirnment = []
    with open(file_path) as file:
        requirnment = file.readlines()
        requirnment = [req.replace("\n", "") for req in requirnment]
        if HYPEN_E_DOT in requirnment:
            requirnment.remove(HYPEN_E_DOT)
    return requirnment


setup(
    name='MLProject',
    author='palash', 
    author_email='palashmoon8@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirnments('requirnments.txt')
)