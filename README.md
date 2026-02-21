# ZHub — Financial Management Portal

ZHub is a Django-based financial management portal for tracking fitness studio revenue, rental property income, and household budgeting.

## Tech Stack

- **Django 5.1** with Python 3.12
- **PostgreSQL** (via `dj-database-url`)
- **Django Allauth** for authentication
- **HTMX** for dynamic interactions
- **Tailwind CSS** (CDN in Phase 1)
- **Chart.js** for dashboard charts
- **Gunicorn** + **WhiteNoise** for production

## Local Development Setup

```bash
# 1. Clone the repo
git clone https://github.com/dunlapwr/zbase.git
cd zbase

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create Django sites record (required by allauth)
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.update_or_create(id=1, defaults={'domain':'localhost:8000','name':'ZHub Local'})"

# 6. Seed demo data
python manage.py seed_demo

# 7. Run the development server
python manage.py runserver
```

Then visit http://localhost:8000 and log in with `owner1` / `zhub1234`.

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | dev fallback (insecure) |
| `DJANGO_SETTINGS_MODULE` | Settings module path | `zhub.settings.development` |
| `DATABASE_URL` | PostgreSQL connection string | SQLite (dev) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `DEBUG` | Enable debug mode | `False` |

## DigitalOcean App Platform Deployment

1. Push code to the `main` branch on GitHub
2. Create a new App on [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
3. Connect your GitHub repo (`dunlapwr/zbase`)
4. Add a **Dev Database** (PostgreSQL)
5. Set environment variables:
   - `DJANGO_SECRET_KEY` — generate with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `DJANGO_SETTINGS_MODULE` = `zhub.settings.production`
   - `DJANGO_ALLOWED_HOSTS` = your app's domain
6. The `.do/app.yaml` spec file is included for reference

The build command runs `collectstatic` and `migrate` automatically.

## Project Structure

```
zbase/
├── apps/
│   ├── accounts/     # Custom user, household, settings
│   ├── dashboard/    # Main dashboard
│   ├── studios/      # Fitness studios (Phase 2)
│   ├── properties/   # Rental properties (Phase 3)
│   └── budget/       # Budgeting (Phase 4)
├── templates/        # All templates organized by app
├── static/           # Static files (CSS, JS, images)
├── zhub/             # Django project config
│   └── settings/     # Split settings (base, development, production)
├── .do/app.yaml      # DigitalOcean App Platform spec
├── manage.py
├── requirements.txt
└── runtime.txt
```

## Demo Accounts

After running `seed_demo`:

| Username | Password | Role |
|---|---|---|
| `owner1` | `zhub1234` | Owner |
| `owner2` | `zhub1234` | Owner |

Both users belong to the same household and share financial data.
