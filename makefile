release: clean
	pip install twine
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*