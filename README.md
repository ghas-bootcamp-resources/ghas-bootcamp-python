# PageTurner Library Admin

PageTurner is a deliberately vulnerable Flask application for GitHub Advanced Security bootcamps. It looks like a small internal library admin tool for a company book club, but it intentionally contains security and code quality issues so participants can enable GHAS and inspect realistic findings.

Do not use this application as a production example.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m server
```

Open `http://localhost:5000`.

If port 5000 is already in use, run `PORT=5001 python -m server` and open `http://localhost:5001`.

Seed users:

| Username | Password | Role |
| --- | --- | --- |
| `admin` | `admin123` | administrator |
| `morgan` | `books2026` | book club coordinator |
| `riley` | `reader` | reader |

## GHAS demo map

| Area | Example | Teaching point |
| --- | --- | --- |
| CodeQL security | Catalog search and login concatenate request values into SQL | User-controlled data flowing into SQL queries |
| CodeQL security | Profiles use `render_template_string` with database content | Reflected and stored cross-site scripting |
| CodeQL security | `/download?file=...` joins user input into a file path | Path traversal through document downloads |
| CodeQL security | `/diagnostics?host=...` builds a shell command from request input | Command injection in support tooling |
| CodeQL security | `/imports/session` deserializes request bytes with `pickle` | Unsafe deserialization of user-controlled data |
| CodeQL security | `/go?next=...` redirects to a request-controlled URL | Open redirect and phishing risk |
| Secret Protection | Training tokens are hardcoded in Flask config | Secret detection and remediation workflow |
| Code Quality | Duplicate dictionary keys, unused local values, empty exception handling, unreachable code, and lambda cleanup helpers | Standard findings and PR comments from GitHub Code Quality |

## Pull request exercises

The file `server/pr_exercises.py` contains commented-out examples that participants can uncomment on a branch. Each block is designed to introduce a new security or Code Quality finding in a pull request.

The file `tests/test_participant_coverage_exercises.py` contains commented-out tests that participants can uncomment to increase code coverage and trigger a coverage report comment on the pull request.

Recommended flow:

1. Enable GitHub Advanced Security features for the copied repository.
2. Run the baseline CodeQL scan on `main` and review the initial findings.
3. Create a branch such as `exercise/add-diagnostics`.
4. Uncomment one block in `server/pr_exercises.py`.
5. Commit the change and open a pull request.
6. Review CodeQL and Code Quality comments on the pull request.

Keep exercises small so participants can see exactly which change introduced each alert.

## Useful demo URLs

| URL | Purpose |
| --- | --- |
| `/` | Catalog dashboard |
| `/?q=Kindred` | Search flow |
| `/profile/riley` | Profile rendering flow |
| `/documents` | Shared document listing |
| `/download?file=welcome.txt` | Document download flow |
| `/diagnostics?host=127.0.0.1` | Support diagnostics flow |
| `/go?next=/documents` | Redirect helper flow |
| `/api/settings` | Code Quality examples in a normal API route |
