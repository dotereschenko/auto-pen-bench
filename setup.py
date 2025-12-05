from setuptools import setup, find_packages

setup(
    name='autopenbench',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv>=1.0.1',  # Fixed typo: => to >=
        'paramiko==3.5.0',
        'termcolor==2.4.0',
        'chardet==5.2.0',
        'pydantic>=2.10.6',
        'ipykernel==6.29.5',
        'pyyaml==6.0.2',
        'openai>=1.109.1',
        'instructor==1.5.0',
        'httpx>=0.28.1'
    ],
    include_package_data=True,
)
