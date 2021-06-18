all: run-dev

run-prod:
	@twistd -y service.tac

run-dev:
	@twistd -noy service.tac

test:
	@python tests/test.py

kill:
	@kill `cat twistd.pid`

clean:
	rm -rf *.log

.FORCE: