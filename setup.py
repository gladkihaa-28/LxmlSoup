from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='LxmlSoup',
  version='1.3.5',
  author='Alexander554',
  author_email='XXXXXXXXXXXXX',
  description='LxmlSoup is a set of tools for fast and easy parsing',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['lxml'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='LxmlSoup',
  python_requires='>=3.7'
)
