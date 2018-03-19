test:
	py.test

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf coverage.xml .coverage.* *.egg-info dist .cache

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$PYPI_USERNAME --password $$PYPI_PASSWORD dist/*