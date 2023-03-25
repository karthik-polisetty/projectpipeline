from setuptools import setup, find_packages

setup(name="src",
      version="0.0.1",
      author="krish",
      author_email="Krish@mail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )