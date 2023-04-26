from setuptools import find_packages, setup
setup(
    name='Project Stardust Auto',
    packages=find_packages(include=['Project_Stardust']),
    version='0.1.2',
    description='Python Library to play the roblox game Project Stardust',
    author='Kaleb Schmidlkofer',
    license='MIT',
    install_requires=['pyautogui', 'pydirectinput', 'keyboard', 'pillow'],
    
)