test:
	tox

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf coverage.xml .coverage.* *.egg-info dist .cache
