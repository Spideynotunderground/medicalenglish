# English for Medical Students Platform

A comprehensive English learning platform designed specifically for medical students. Built with Django REST Framework backend and React frontend.

## Features

- 📚 **15 Units** covering medical English topics and grammar
- 📝 **13 Task Types** per unit including:
  - Fill in the blanks
  - Multiple choice
  - Matching (drag & drop)
    - Translation (AI evaluated)
  - Speaking practice (AI evaluated)
  - Writing tasks (AI evaluated)
  - Video retelling (AI evaluated)
- 🎯 **Progress tracking** with points, levels, and streaks
- 🏆 **Leaderboard** to compete with other students
- 🔐 **JWT Authentication** for secure access
- 📱 **Responsive design** for mobile and desktop

## Tech Stack

- **Backend**: Django 5.0, Django REST Framework
- **Frontend**: React 18, Vite, Tailwind CSS
- **Database**: SQLite (can be switched to PostgreSQL)
- **AI**: OpenAI GPT-4o-mini for evaluation
- **Authentication**: JWT tokens

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend development only)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd english-medical
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Run deployment script**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

4. **Seed the database**
   ```bash
   source venv/bin/activate
   python manage.py seed_data
   ```

5. **Run the server**
   ```bash
   # Development
   python manage.py runserver 0.0.0.0:8000
   
   # Production
   gunicorn config.wsgi:application --bind 0.0.0.0:8000
   ```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Debug mode (True/False) | No (default: False) |
| `OPENAI_API_KEY` | OpenAI API key for AI evaluation | Yes (for AI features) |

## Project Structure

```
backend/
├── api/                    # Main API application
│   ├── management/         # Management commands
│   │   └── commands/       # Seed data files
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── services.py        # AI evaluation service
│   └── urls.py            # API routes
├── config/                 # Django configuration
│   ├── settings.py        # Settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI application
├── static/                 # Static files (PDFs, etc.)
├── staticfiles/            # Built React frontend
├── templates/              # HTML templates
├── manage.py              # Django management
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku/deployment config
└── deploy.sh              # Deployment script
```

## API Endpoints

### Authentication
- `POST /api/register/` - Register new user
- `POST /api/login/` - Login and get tokens
- `POST /api/token/refresh/` - Refresh access token

### Units & Tasks
- `GET /api/units/` - List all units
- `GET /api/units/{id}/` - Get unit details with tasks
- `GET /api/tasks/{id}/` - Get task with questions
- `POST /api/tasks/{id}/submit/` - Submit task answers

### User Progress
- `GET /api/progress/` - Get user progress
- `GET /api/leaderboard/` - Get leaderboard
- `GET /api/profile/` - Get user profile

### Vocabulary
- `GET /api/vocabulary/` - Get vocabulary list
- `GET /api/idioms/` - Get medical idioms
- `GET /api/phrasal-verbs/` - Get phrasal verbs

## Deployment

### Heroku

```bash
heroku create english-medical
heroku config:set SECRET_KEY=your-secret-key
heroku config:set OPENAI_API_KEY=your-openai-key
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py seed_data
```

### VPS/Server

1. Upload files to server
2. Set up virtual environment
3. Run `./deploy.sh`
4. Configure Nginx/Apache as reverse proxy
5. Set up SSL certificate

### cPanel (Passenger)

1. Upload files to public_html
2. Set up Python application in cPanel
3. Configure passenger_wsgi.py
4. Set environment variables in .htaccess

## License

MIT License

## Author

Developed for medical students learning English.
