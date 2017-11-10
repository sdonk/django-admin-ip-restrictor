test:
	py.test

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf coverage.xml .coverage.* *.egg-info dist .cache

release: clean
	pip install twine
	python setup.py sdist bdist_wheel
	twine upload dist/*