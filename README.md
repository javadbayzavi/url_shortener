# URL Shortener

A small URL-shortener service implemented in Python.
Repository layout indicates a modular structure with clear separation between API, core logic, and services; containerization and tests are included.

## Repository structure
```
url_shortener/
├── api/                  # HTTP API (endpoints / routing)
├── core/                 # Core domain logic (models / utilities)
├── services/             # Service layer (storage / shortener logic)
├── tests/                # Unit and integration tests
├── .env                  # Example environment variables
├── DockerFile            # Container image definition
├── docker-compose.yml    # Local stack (db, service orchestration)
├── main.py               # Application entrypoint
└── requirement.txt       # Python dependencies
```

## Quick start

### 1) With Docker (recommended)

Make sure Docker is running, then:
```
docker-compose up --build
```
This will build the image and start the application together with any linked services defined in docker-compose.yml.

### 2) Locally (venv)
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
python main.py
```
$$$ main.py $$$ is the application entrypoint — run it to start the API server locally.


### What to expect
-	The api/ folder contains the web endpoints.
-	The core/ folder contains the business logic and data models.
-	The services/ folder contains persistence or helper services (e.g., DB adapter, hashing/ID generator).
-	tests/ includes unit / integration tests (run with pytest).

### Typical features for this kind of project (confirm by inspecting the code directly):
-	Create a shortened URL for a long URL
-	Redirect a short code to the original URL
-	Optional: stats/analytics for a short URL (click count, creation date)
-	Configurable storage (in-memory / file / DB) implemented under services/


## Running tests
```
pip install -r requirement.txt
pytest
```
If the test suite uses containers (db, redis), docker-compose.yml may spin up required services during tests.


## Environment

Provide configuration via .env (example file exists in repo). Typical variables:
	•	PORT — service port
	•	DATABASE_URL — DB connection (if used)
	•	REDIS_URL — cache (if used)
	•	SECRET_KEY — signing / token secret (if used)

## Notes & next steps
	•	The project is already containerized — good for local dev and demos.
	•	If you want a small frontend, a static HTML page with a shortener form is trivial to add.
	•	If analytics are required, add an endpoint under api/ to expose click counts and basic metadata.


## License
MIT
