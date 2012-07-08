test:
	nosetests tests

coverage:
	nosetests --with-coverage --cover-html --cover-package=miner
	
pep8:
	pep8 miner tests
	
clean:
	rm .coverage
	rm -r cover
