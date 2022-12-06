Blog
https://wangonya.com/blog/publishing-package-on-test-pypi/

# install dependencies
pip install pipdeptree
pip install twine 

# build your python codebase
python setup.py sdist bdist_wheel

# publist to testpypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# publish to pypi
twine upload dist/*