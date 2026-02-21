# ZHub — Claude Code Instructions

## Project Overview

ZHub is a Django 5.1 financial management app (studios, rental properties, budgeting).
It runs on **Heroku** with Postgres and uses django-allauth for auth.

## Tech Stack

- **Backend**: Django 5.1, gunicorn, whitenoise, dj-database-url
- **Auth**: django-allauth (email-based login)
- **Database**: PostgreSQL (Heroku Postgres)
- **Frontend**: Django templates + Tailwind CSS (via CDN) + htmx
- **Deployment**: Heroku (auto-deploys from `main` branch)

## Git Workflow

**Always work directly on the `main` branch. Never create feature branches.**

After making ANY changes:

1. Pull latest first: `git pull origin main`
2. Stage your changes: `git add <specific files>`
3. Commit with a clear message: `git commit -m "description of what changed"`
4. Push immediately: `git push origin main`

**Every push to `main` triggers an automatic deploy to Heroku.** Do not skip the push step.

## Project Structure

```
zhub/                   # Django project settings
  settings/
    base.py             # Shared settings
    development.py      # Local dev (SQLite, DEBUG=True)
    production.py       # Heroku (Postgres, DEBUG=False)
apps/
  accounts/             # Custom user model, household, profile settings
  dashboard/            # Main dashboard with summary cards
  studios/              # Fitness studio management
  properties/           # Rental property portfolio, units, leases
  budget/               # Budget & cash flow (Phase 4 — not yet built)
templates/              # All Django templates (Tailwind-styled)
static/                 # Static assets
```

## Key Conventions

- Templates live in `templates/` (not inside each app)
- All templates extend `base.html` which provides the sidebar, top bar, and flash messages
- Forms use Tailwind CSS classes applied via widget attrs in the form class
- Views use `@login_required` and filter by `request.user.household`
- Use `messages.success()` / `messages.error()` for user feedback after actions

## Running Locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo          # creates demo users and data
python manage.py runserver
```

Demo login: `owner1@zhub.local` / `zhub1234`

## Common Commands

- `python manage.py makemigrations` — after model changes
- `python manage.py migrate` — apply migrations
- `python manage.py check --deploy` — verify production readiness
- `python manage.py collectstatic --noinput` — collect static files (Heroku does this at build time)
