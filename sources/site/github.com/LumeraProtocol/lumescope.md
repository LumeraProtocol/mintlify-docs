# Source: https://github.com/LumeraProtocol/lumescope

### Uh oh!

There was an error while loading. [Please reload this page]().

[LumeraProtocol](https://github.com/LumeraProtocol) / **[lumescope](https://github.com/LumeraProtocol/lumescope)** Public

- [Notifications](https://github.com/login?return_to=%2FLumeraProtocol%2Flumescope) You must be signed in to change notification settings
- [Fork 2](https://github.com/login?return_to=%2FLumeraProtocol%2Flumescope)
- [Star 1](https://github.com/login?return_to=%2FLumeraProtocol%2Flumescope)
 

 

 master

[Branches](https://github.com/LumeraProtocol/lumescope/branches) [Tags](https://github.com/LumeraProtocol/lumescope/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

## Latest commit

## History

[20 Commits](https://github.com/LumeraProtocol/lumescope/commits/master/)

20 Commits

 |
| 

[.vscode](https://github.com/LumeraProtocol/lumescope/tree/master/.vscode '.vscode')

 | 

[.vscode](https://github.com/LumeraProtocol/lumescope/tree/master/.vscode '.vscode')

 | 

 | 

 |
| 

[cmd/lumescope](https://github.com/LumeraProtocol/lumescope/tree/master/cmd/lumescope 'This path skips through empty directories')

 | 

[cmd/lumescope](https://github.com/LumeraProtocol/lumescope/tree/master/cmd/lumescope 'This path skips through empty directories')

 | 

 | 

 |
| 

[docs](https://github.com/LumeraProtocol/lumescope/tree/master/docs 'docs')

 | 

[docs](https://github.com/LumeraProtocol/lumescope/tree/master/docs 'docs')

 | 

 | 

 |
| 

[internal](https://github.com/LumeraProtocol/lumescope/tree/master/internal 'internal')

 | 

[internal](https://github.com/LumeraProtocol/lumescope/tree/master/internal 'internal')

 | 

 | 

 |
| 

[scripts](https://github.com/LumeraProtocol/lumescope/tree/master/scripts 'scripts')

 | 

[scripts](https://github.com/LumeraProtocol/lumescope/tree/master/scripts 'scripts')

 | 

 | 

 |
| 

[.dockerignore](https://github.com/LumeraProtocol/lumescope/blob/master/.dockerignore '.dockerignore')

 | 

[.dockerignore](https://github.com/LumeraProtocol/lumescope/blob/master/.dockerignore '.dockerignore')

 | 

 | 

 |
| 

[.env.example](https://github.com/LumeraProtocol/lumescope/blob/master/.env.example '.env.example')

 | 

[.env.example](https://github.com/LumeraProtocol/lumescope/blob/master/.env.example '.env.example')

 | 

 | 

 |
| 

[.gitignore](https://github.com/LumeraProtocol/lumescope/blob/master/.gitignore '.gitignore')

 | 

[.gitignore](https://github.com/LumeraProtocol/lumescope/blob/master/.gitignore '.gitignore')

 | 

 | 

 |
| 

[Dockerfile](https://github.com/LumeraProtocol/lumescope/blob/master/Dockerfile 'Dockerfile')

 | 

[Dockerfile](https://github.com/LumeraProtocol/lumescope/blob/master/Dockerfile 'Dockerfile')

 | 

 | 

 |
| 

[Makefile](https://github.com/LumeraProtocol/lumescope/blob/master/Makefile 'Makefile')

 | 

[Makefile](https://github.com/LumeraProtocol/lumescope/blob/master/Makefile 'Makefile')

 | 

 | 

 |
| 

[README.md](https://github.com/LumeraProtocol/lumescope/blob/master/README.md 'README.md')

 | 

[README.md](https://github.com/LumeraProtocol/lumescope/blob/master/README.md 'README.md')

 | 

 | 

 |
| 

[entrypoint.sh](https://github.com/LumeraProtocol/lumescope/blob/master/entrypoint.sh 'entrypoint.sh')

 | 

[entrypoint.sh](https://github.com/LumeraProtocol/lumescope/blob/master/entrypoint.sh 'entrypoint.sh')

 | 

 | 

 |
| 

[go.mod](https://github.com/LumeraProtocol/lumescope/blob/master/go.mod 'go.mod')

 | 

[go.mod](https://github.com/LumeraProtocol/lumescope/blob/master/go.mod 'go.mod')

 | 

 | 

 |
| 

[go.sum](https://github.com/LumeraProtocol/lumescope/blob/master/go.sum 'go.sum')

 | 

[go.sum](https://github.com/LumeraProtocol/lumescope/blob/master/go.sum 'go.sum')

 | 

 | 

 |
| 

View all files

 |

## Repository files navigation

# LumeScope

[![Go](https://camo.githubusercontent.com/94d550782386415e0880e25d8586f05dbea14d195b285de74a5637c3cb7d5d66/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f2d312e32342b2d3030414444383f6c6f676f3d676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/94d550782386415e0880e25d8586f05dbea14d195b285de74a5637c3cb7d5d66/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f2d312e32342b2d3030414444383f6c6f676f3d676f266c6f676f436f6c6f723d7768697465) [![Docker](https://camo.githubusercontent.com/4a3dff01d2525c50ee53d2180c15e9c18af89376ae1ef68288d982a168b61631/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d72656164792d3234393645443f6c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/4a3dff01d2525c50ee53d2180c15e9c18af89376ae1ef68288d982a168b61631/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d72656164792d3234393645443f6c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465) [![License](https://camo.githubusercontent.com/784362b26e4b3546254f1893e778ba64616e362bd6ac791991d2c9e880a3a64e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667)](https://camo.githubusercontent.com/784362b26e4b3546254f1893e778ba64616e362bd6ac791991d2c9e880a3a64e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667)

**LumeScope** is a neutral, read-only API aggregator for the Lumera network. It decodes Action metadata (Cascade/Sense), provides Cascade previews (MIME types, file sizes), and aggregates SuperNode metrics, probes, version compatibility, and payment statistics—so Lumera clients stay lightweight and responsive.

## Features

- **Actions API** — List and detail endpoints for decoded Action metadata (Cascade/Sense types) with transaction lifecycle tracking (register, finalize, approve)
- **SuperNode Metrics** — Aggregated hardware stats, version matrix, payment info, and availability probes
- **Background Scheduler** — Automatic sync loops:
 - Validators sync (default: 5m)
 - SuperNodes sync (default: 2m)
 - Actions sync (default: 30s)
 - SuperNode port probes (default: 1m)
 - Action transaction enricher (background)
- **Embedded PostgreSQL 14** — Single-container deployment; no external database required
- **Swagger UI** — Interactive API docs at `/docs`
- **OpenAPI 3.0** — Machine-readable spec at `/openapi.json`
- **stdlib-only HTTP** — No third-party web frameworks; uses Go's `net/http`

## API Reference

LumeScope exposes **16 endpoints**. All data is read-only.

| Endpoint | Method | Description | Key Params | Example |
| --- | --- | --- | --- | --- |
| `/healthz` | GET | Liveness probe (always 200 if running) | — | `curl http://localhost:18080/healthz` |
| `/readyz` | GET | Readiness probe | — | `curl http://localhost:18080/readyz` |
| `/v1/actions` | GET | List actions with decoded metadata | `type`, `creator`, `state`, `supernode`, `fromHeight`, `toHeight`, `limit`, `cursor`, `include_transactions` | `curl 'http://localhost:18080/v1/actions?type=cascade&limit=5'` |
| `/v1/actions/{id}` | GET | Action details with transactions | — | `curl http://localhost:18080/v1/actions/action123` |
| `/v1/actions/stats` | GET | Aggregated action statistics | `from`, `to` (RFC3339), `type` | `curl 'http://localhost:18080/v1/actions/stats?type=cascade'` |
| `/v1/supernodes/metrics` | GET | List supernode metrics | `currentState`, `status`, `version`, `minFailedProbeCounter`, `limit`, `cursor` | `curl 'http://localhost:18080/v1/supernodes/metrics?status=available&limit=10'` |
| `/v1/supernodes/{id}/metrics` | GET | Single supernode metrics | — | `curl http://localhost:18080/v1/supernodes/lumera1abc.../metrics` |
| `/v1/supernodes/{id}/paymentInfo` | GET | Payment statistics by denomination | — | `curl http://localhost:18080/v1/supernodes/lumera1abc.../paymentInfo` |
| `/v1/supernodes/stats` | GET | Aggregated hardware statistics | — | `curl http://localhost:18080/v1/supernodes/stats` |
| `/v1/supernodes/action-stats` | GET | Action statistics per supernode | — | `curl http://localhost:18080/v1/supernodes/action-stats` |
| `/v1/supernodes/unavailable` | GET | Supernodes with unavailable status API | `currentState` | `curl http://localhost:18080/v1/supernodes/unavailable` |
| `/v1/supernodes/sync` | POST | Trigger manual sync+probe (if enabled) | — | `curl -X POST http://localhost:18080/v1/supernodes/sync` |
| `/v1/version/matrix` | GET | Version compatibility matrix (partial LEP2) | — | `curl http://localhost:18080/v1/version/matrix` |
| `/openapi.json` | GET | OpenAPI 3.0 specification | — | `curl http://localhost:18080/openapi.json` |
| `/docs` | GET | Swagger UI documentation | — | Open in browser: `http://localhost:18080/docs` |
| `/metrics` | GET | Prometheus metrics (**stub**) | — | `curl http://localhost:18080/metrics` |

> **Note:** `/metrics` currently returns stub data. Rate limiting is planned for future releases.

See also: [`docs/openapi.json`](https://github.com/LumeraProtocol/lumescope/blob/master/docs/openapi.json) and [`docs/context.json`](https://github.com/LumeraProtocol/lumescope/blob/master/docs/context.json) for implementation details.

## Quickstart

### 1\. Build the Docker image

```shell
docker build -t lumescope .
```

Build output is ~358 MB.

### 2\. Run the container

**Minimal (ephemeral, for testing):**

```shell
docker run -d -p 18080:18080 -e LUMERA_API_BASE=https://lcd.lumera.io --name lumescope lumescope
```

**With custom environment file:**

```shell
cp .env.example .env
# Edit .env with your settings (see Configuration below)

docker run -d -p 18080:18080 \
  -v $(pwd)/.env:/app/.env \
  --name lumescope lumescope
```

### 3\. Verify deployment

```shell
# Health check
curl -i http://localhost:18080/healthz

# Readiness check
curl -i http://localhost:18080/readyz

# Fetch recent actions
curl -s 'http://localhost:18080/v1/actions?limit=3' | jq .

# Open Swagger UI in browser
open http://localhost:18080/docs
```

### 4\. Stop and remove container

```shell
docker stop lumescope
docker rm lumescope
```

## Configuration

Copy [`.env.example`](https://github.com/LumeraProtocol/lumescope/blob/master/.env.example) to `.env` and customize as needed. The container reads environment variables at startup.

### Environment Variables

| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `LUMERA_API_BASE` | **Yes** | `http://localhost:1317` | Lumera REST (LCD) endpoint URL |
| `PORT` | No | `18080` | HTTP server listen port |
| `CORS_ALLOW_ORIGINS` | No | `*` | Comma-separated CORS origins |
| `DB_DSN` | No | `postgres://postgres:postgres@localhost:5432/lumescope?sslmode=disable` | PostgreSQL connection string (for external DB) |
| `DB_MAX_CONNS` | No | `10` | Max database connections |
| `HTTP_TIMEOUT` | No | `10s` | Outbound HTTP timeout for Lumera calls |
| `READ_HEADER_TIMEOUT` | No | `5s` | Server read header timeout |
| `READ_TIMEOUT` | No | `30s` | Server read timeout |
| `WRITE_TIMEOUT` | No | `30s` | Server write timeout |
| `IDLE_TIMEOUT` | No | `120s` | Server idle timeout |
| `REQUEST_TIMEOUT` | No | `10s` | Per-request server timeout |
| `VALIDATORS_SYNC_INTERVAL` | No | `5m` | Validators sync frequency |
| `SUPERNODES_SYNC_INTERVAL` | No | `2m` | SuperNodes sync frequency |
| `ACTIONS_SYNC_INTERVAL` | No | `30s` | Actions sync frequency |
| `PROBE_INTERVAL` | No | `1m` | SuperNode probe frequency |
| `DIAL_TIMEOUT` | No | `2s` | TCP dial timeout for probes |

### Embedded PostgreSQL Variables (Docker only)

| Variable | Default | Description |
| --- | --- | --- |
| `POSTGRES_DB` | `lumescope` | Database name |
| `POSTGRES_USER` | `postgres` | Database user |
| `POSTGRES_PASSWORD` | `postgres` | Database password (set for security) |
| `PGDATA` | `/var/lib/postgresql/data` | Data directory |

**Recommendation:** Set `POSTGRES_PASSWORD` to a strong value in production:

```shell
docker run -d -p 18080:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e POSTGRES_PASSWORD=your-secure-password \
  --name lumescope lumescope
```

## Production Deployment

### Persistent Data Volume

Mount a volume to retain PostgreSQL data across container restarts:

```shell
docker run -d -p 18080:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e POSTGRES_PASSWORD=your-secure-password \
  -v lumescope_data:/var/lib/postgresql/data \
  --name lumescope lumescope
```

### Using Makefile Targets

The [`Makefile`](https://github.com/LumeraProtocol/lumescope/blob/master/Makefile) provides convenience targets:

```shell
# Mainnet with persistent volume
make docker-run-mainnet

# Testnet with persistent volume
make docker-run-testnet

# Ephemeral local development
make docker-run-local
```

### External PostgreSQL Database

To use an external PostgreSQL 13+ database instead of the embedded one:

```shell
docker run -d -p 18080:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e DB_DSN="postgres://user:pass@your-pg-host:5432/lumescope?sslmode=require" \
  --name lumescope lumescope
```

The application auto-creates required tables and indexes on startup.

### Running Multiple Replicas

For high availability, run multiple LumeScope containers pointing to a shared external PostgreSQL:

```shell
# Instance 1
docker run -d -p 18081:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e DB_DSN="postgres://user:pass@pg-host:5432/lumescope?sslmode=require" \
  --name lumescope-1 lumescope

# Instance 2
docker run -d -p 18082:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e DB_DSN="postgres://user:pass@pg-host:5432/lumescope?sslmode=require" \
  --name lumescope-2 lumescope
```

Place a load balancer (nginx, HAProxy, cloud LB) in front of the instances.

### Monitoring

- **Health endpoint:** `GET /healthz` (liveness)
- **Readiness endpoint:** `GET /readyz`
- **Metrics endpoint:** `GET /metrics` (currently returns stub data; Prometheus integration planned)

The Docker image includes a built-in `HEALTHCHECK` that polls `/healthz` every 30 seconds.

### Future Enhancements

- Full Prometheus metrics export
- Rate limiting per client
- Redis caching layer for sub-200ms p95 latency

## Publishing to Public Registry (For Repo Owners)

### Docker Hub

Assumes you have already built a local `lumescope` image (see [Quickstart](https://github.com/#quickstart)).

```shell
# Login to Docker Hub
docker login

# Tag the local image
docker tag lumescope yourusername/lumescope:v1.0.0

# Push to Docker Hub
docker push yourusername/lumescope:v1.0.0

# (Optional) Also push a :latest tag
docker tag lumescope yourusername/lumescope:latest
docker push yourusername/lumescope:latest
```

### GitHub Container Registry (GHCR)

GHCR requires a **classic Personal Access Token (PAT)** with the correct scopes. If you see `denied: permission_denied: The token provided does not match expected scopes`, your token is missing required permissions.

**1\. Create a classic PAT:**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens) → **Generate new token (classic)**.
2. Select scopes:
 - `repo` (full control) — required if the package repository is private.
 - `read:packages` — pull images.
 - `write:packages` — push images.
3. Copy the token; you won't see it again.

**2\. (Org only) Ensure package write permissions:**

If publishing under an **organization**, your user must have write access to packages:

1. Navigate to **Organization → Settings → Packages**.
2. Under _Package creation_, ensure members can publish packages.
3. Verify you are a member with appropriate role (e.g., _Maintainer_ or _Admin_).

**3\. Authenticate and push:**

```shell
# Set environment variables (or substitute directly)
export GITHUB_PAT=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export GITHUB_USERNAME=yourusername

# Login to GHCR
echo $GITHUB_PAT | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin

# Tag the local image (replace {owner} with your username or org)
docker tag lumescope ghcr.io/{owner}/lumescope:v1.0.0

# Push to GHCR
docker push ghcr.io/{owner}/lumescope:v1.0.0

# (Optional) Also push a :latest tag
docker tag lumescope ghcr.io/{owner}/lumescope:latest
docker push ghcr.io/{owner}/lumescope:latest
```

### Multi-Architecture Builds

For ARM64 and AMD64 support using `docker buildx`:

```shell
docker buildx create --use

# Docker Hub
docker buildx build --platform linux/amd64,linux/arm64 \
  -t yourusername/lumescope:v1.0.0 \
  --push .

# GHCR
docker buildx build --platform linux/amd64,linux/arm64 \
  -t ghcr.io/{owner}/lumescope:v1.0.0 \
  --push .
```

### Credential Helper (Avoid Unencrypted Warnings)

If Docker warns about storing credentials unencrypted, configure a credential helper:

```shell
# Example: use the native OS keychain (macOS/Windows) or pass (Linux)
# See: https://docs.docker.com/engine/reference/commandline/login/#credential-helpers
docker-credential-helper  # varies by OS
```

On Linux, install `pass` and `docker-credential-pass`, then configure `~/.docker/config.json`:

```json
{
  "credsStore": "pass"
}
```

## Development

### Prerequisites

- Go 1.24+
- PostgreSQL 13+ (or use Docker)

### Building Locally

```shell
# Build binary
make build
# or: go build -o bin/lumescope ./cmd/lumescope

# Run directly
./bin/lumescope

# Or run without building
go run ./cmd/lumescope
```

### Makefile Targets

| Target | Description |
| --- | --- |
| `make build` | Build the Go binary to `bin/lumescope` |
| `make docker-build` | Build the Docker image |
| `make docker-run` | Run ephemeral container (local dev) |
| `make docker-run-local` | Alias for `docker-run` |
| `make docker-run-mainnet` | Run with mainnet LCD + persistent volume |
| `make docker-run-testnet` | Run with testnet LCD + persistent volume |
| `make docker-stop` | Stop the lumescope container |
| `make docker-rm` | Remove the lumescope container |
| `make docker-rebuild` | Stop, remove, rebuild, and run |

### Project Structure

```
├── cmd/lumescope/       # Application entrypoint
├── internal/
│   ├── background/      # Scheduler and sync loops
│   ├── config/          # Environment configuration
│   ├── db/              # PostgreSQL operations
│   ├── decoder/         # Protobuf metadata decoder
│   ├── handlers/        # HTTP route handlers
│   ├── lumera/          # Lumera LCD client
│   ├── server/          # HTTP router setup
│   └── util/            # JSON helpers
├── docs/
│   ├── context.json     # Implementation status reference
│   ├── requirements.json # Project requirements
│   ├── openapi.json     # OpenAPI 3.0 spec (JSON)
│   └── openapi.yaml     # OpenAPI 3.0 spec (YAML)
├── Dockerfile           # Multi-stage build with embedded Postgres
├── Makefile             # Build and run targets
└── .env.example         # Environment variable template
```

## Troubleshooting

### LCD endpoint unreachable

**Symptom:** Actions/supernodes not syncing; logs show connection errors.

**Solution:**

1. Verify `LUMERA_API_BASE` is set correctly:
 
 ```shell
    curl https://lcd.lumera.io/cosmos/base/tendermint/v1beta1/node_info
    ```
 
2. Check network connectivity from the container:
 
 ```shell
    docker exec lumescope wget -qO- https://lcd.lumera.io/healthz
    ```
 
3. If using a local node, ensure the LCD port (1317) is exposed.

### Database connection failures

**Symptom:** Startup fails or queries timeout.

**Solution:**

1. For embedded Postgres, check container logs:
 
 ```shell
    docker logs lumescope
    ```
 
2. For external Postgres, verify `DB_DSN`:
 
 ```shell
    psql "postgres://user:pass@host:5432/lumescope?sslmode=disable" -c "\dt"
    ```
 
3. Ensure the database user has CREATE TABLE privileges.

### SuperNode probe failures

**Symptom:** Supernodes show as unavailable; probe metrics missing.

**Cause:** SuperNode ports 4444, 4445, or 8002 may be firewalled or the status API is disabled by operators.

**Solution:**

1. This is expected for some supernodes.
2. Check `/v1/supernodes/unavailable` to see affected nodes.
3. The `failedProbeCounter` field tracks consecutive failures.

### CORS errors in browser

**Symptom:** Browser console shows CORS policy errors.

**Solution:** Set `CORS_ALLOW_ORIGINS` to your frontend origin:

```shell
docker run -d -p 18080:18080 \
  -e LUMERA_API_BASE=https://lcd.lumera.io \
  -e CORS_ALLOW_ORIGINS="https://your-app.com" \
  --name lumescope lumescope
```

Use `*` only for development.

---

## License

MIT License. See [LICENSE](https://github.com/LumeraProtocol/lumescope/blob/master/LICENSE) for details.

## About

No description, website, or topics provided.

### Resources

[Readme](https://github.com/#readme-ov-file)

### Uh oh!

There was an error while loading. [Please reload this page]().

[Activity](https://github.com/LumeraProtocol/lumescope/activity)

[Custom properties](https://github.com/LumeraProtocol/lumescope/custom-properties)

### Stars

[**1** star](https://github.com/LumeraProtocol/lumescope/stargazers)

### Watchers

[**0** watching](https://github.com/LumeraProtocol/lumescope/watchers)

### Forks

[**2** forks](https://github.com/LumeraProtocol/lumescope/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FLumeraProtocol%2Flumescope&report=LumeraProtocol+%28user%29)

## [Releases](https://github.com/LumeraProtocol/lumescope/releases)

[1 tags](https://github.com/LumeraProtocol/lumescope/tags)

## [Packages 0](https://github.com/orgs/LumeraProtocol/packages?repo_name=lumescope)

### Uh oh!

There was an error while loading. [Please reload this page]().

### Uh oh!

There was an error while loading. [Please reload this page]().

## [Contributors](https://github.com/LumeraProtocol/lumescope/graphs/contributors)

### Uh oh!

There was an error while loading. [Please reload this page]().

## Languages

- [Go 90.0%](https://github.com/LumeraProtocol/lumescope/search?l=go)
- [Shell 8.7%](https://github.com/LumeraProtocol/lumescope/search?l=shell)
- Other 1.3%