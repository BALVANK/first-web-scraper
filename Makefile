UV := uv run

.PHONY: docs

docs:
	cd ./docs/ && uv run make livehtml
