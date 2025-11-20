# URL Shortener

A small URL-shortener service implemented in Python.
Repository layout indicates a modular structure with clear separation between API, core logic, and services; containerization and tests are included.

## Application Architecture Overview
This URL shortener application is designed to efficiently manage URL shortening, retrieval, and analytics while ensuring high performance and reliability. The key components and technologies are as follows:
### Database (PostgreSQL):
The application uses PostgreSQL as its primary datastore. All original URLs, shortened URLs, and associated metadata (such as creation date, user info, and hit counts) are persisted in PostgreSQL. This ensures durability, transactional integrity, and strong relational querying capabilities for managing URL data.
### Caching (Redis):
To accelerate URL lookups and reduce database load, the application uses Redis as a caching layer. Frequently accessed URLs are stored in Redis, allowing for near-instant retrieval. This reduces latency and improves scalability, especially under high traffic scenarios.
### API Rate Limiting:
The application includes an API rate limiter to protect the service from abuse and ensure fair usage. This limits the number of requests a client can make within a specific time window, improving stability and preventing overload.
### Service Flow:
1.	When a URL is shortened, it is saved in PostgreSQL.
2.	Frequently accessed URLs are cached in Redis for fast retrieval.
3.	API requests are monitored via the rate limiter to enforce usage policies.
4.	Users can retrieve the original URL via the shortened link, leveraging Redis for speed and PostgreSQL for persistence when cache misses occur.
### Testing & Reliability:
While not part of production usage, the test setup uses Testcontainers to spin up ephemeral PostgreSQL and Redis instances, allowing reproducible, isolated testing environments.

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
main.py is the application entrypoint — run it to start the API server locally.


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


## Test environment (Testcontainers)
The test suite uses Testcontainers to spin up real ephemeral infrastructure during tests (e.g., PostgreSQL or Redis, depending on the test).
Each test run automatically launches lightweight disposable containers, executes the tests against them, and destroys the containers afterward.

This ensures:
-	reproducible, isolated test environments
-	real integration tests instead of mocks
-	zero manual setup on the developer machine
```
pytest
```
will trigger Testcontainers to start the required services automatically.

## Environment

Provide configuration via .env (example file exists in repo). Typical variables:
-	PORT — service port
-	DATABASE_URL — DB connection (if used)
-	REDIS_URL — cache (if used)
-	SECRET_KEY — signing / token secret (if used)

## Notes & next steps
-	The project is already containerized — good for local dev and demos.
-	If you want a small frontend, a static HTML page with a shortener form is trivial to add.
-	If analytics are required, add an endpoint under api/ to expose click counts and basic metadata.


## License
MIT
