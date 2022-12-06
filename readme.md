
# install dependencies
pip install pipdeptree
pip install twine 

# build your python codebase
python setup.py sdist bdist_wheel

# publish to pypi
python -m twine upload dist/*