# CI/CD FastAPI

A minimal FastAPI application with a GitHub Actions CI/CD workflow that builds a Docker image, runs a smoke test, and pushes the image to Docker Hub.

## Project structure

ci-cd-fastapi/
│── main.py
│── requirements.txt
│── Dockerfile
│── .dockerignore
│── tests/
│    └── test_main.py
│── .github/
│    └── workflows/
│         └── ci.yml


## Run locally (Python)

1. Create a venv and install deps:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

2. Run app with uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/


## Run locally (Docker)

1. Build image:

```bash
docker build -t ci-cd-fastapi:local .
```

2. Run container:

```bash
docker run --rm -p 8000:8000 ci-cd-fastapi:local
```

3. Verify:

- http://localhost:8000/
- http://localhost:8000/health


## GitHub Actions CI/CD

- The workflow runs on pushes and PRs to `main`.
- Steps: install deps, run tests, build Docker image, run smoke test by running the container and hitting the endpoint, then login and push image to Docker Hub.

### Required GitHub Secrets

Set the following repository secrets:

- `DOCKER_USERNAME` — your Docker Hub username
- `DOCKER_PASSWORD` — a Docker Hub password or access token

The workflow tags the image as `${{ secrets.DOCKER_USERNAME }}/fastapi-ci:latest` and `${{ secrets.DOCKER_USERNAME }}/fastapi-ci:${{ github.sha }}`.


## Notes

- The workflow assumes `docker` is available on the runner (standard for Ubuntu runners).
- If you want the image pushed for other branches, adjust the `on:` section in `.github/workflows/ci.yml`.
