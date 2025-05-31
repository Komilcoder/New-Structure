.PHONY: run

run:
	PYTHONPATH=. uvicorn main:app --reload
