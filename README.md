# Django REST Assignment - Task Manager

A Django-based task management application that allows users to create, read, update, and delete tasks with additional features like reporting and external API integration.

## 🌐 Live Application

**Live Link:** [https://rest-django-assignment-1.onrender.com/](https://rest-django-assignment-1.onrender.com/)

## 🎥 Demo Video

**Demo Video Link:** [https://www.loom.com/share/8e97c263f5a840d69463b8ef2b98ff2e?sid=18a815e1-7cfa-4cd9-ba03-a7990e80a789](https://www.loom.com/share/8e97c263f5a840d69463b8ef2b98ff2e?sid=18a815e1-7cfa-4cd9-ba03-a7990e80a789)

## ✨ Features

- **Task Management**: Create, read, update, and delete tasks
- **Task Properties**: Each task includes:
  - Task description
  - Assignee
  - Due date
  - Priority level
- **Reporting**: View task statistics with charts showing:
  - Tasks by assignee
  - Tasks by priority level
- **External API Integration**: Fetch and display posts from JSONPlaceholder API
- **Responsive Design**: Clean and modern UI
- **Deployment Ready**: Configured for production deployment on Render

## 🚀 How to Run the App Locally

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd REST-assignment
```

### Step 2: Create and Activate Virtual Environment

**On Windows:**
```bash
# Create virtual environment
python -m venv rest

# Activate virtual environment
rest\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv rest

# Activate virtual environment
source rest/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r rest_project/requirements.txt
```

### Step 4: Navigate to Project Directory

```bash
cd rest_project
```

### Step 5: Run Database Migrations

```bash
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 📁 Project Structure

```
REST-assignment/
├── rest/                          # Virtual environment
├── rest_project/                  # Main Django project
│   ├── manage.py                  # Django management script
│   ├── requirements.txt           # Python dependencies
│   ├── db.sqlite3                # SQLite database (local)
│   ├── rest_project/             # Project settings
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # Main URL configuration
│   │   ├── wsgi.py               # WSGI configuration
│   │   └── asgi.py               # ASGI configuration
│   └── task_manager/             # Task management app
│       ├── models.py             # Task model definition
│       ├── views.py              # View functions
│       ├── urls.py               # App URL configuration
│       ├── admin.py              # Django admin configuration
│       ├── migrations/           # Database migrations
│       └── templates/            # HTML templates
│           ├── index.html        # Home page
│           ├── task_list.html    # Task listing page
│           ├── task_form.html    # Task creation/editing form
│           ├── task_confirm_delete.html # Task deletion confirmation
│           ├── report.html       # Task reporting page
│           ├── external_posts.html # External API integration page
│           └── bat.html          # Additional template
├── Procfile                      # Deployment configuration
└── render.yaml                   # Render deployment configuration
```

## 🛠️ Technologies Used

- **Backend**: Django 5.2.6
- **Database**: SQLite (local), PostgreSQL (production)
- **Static Files**: WhiteNoise
- **Deployment**: Render
- **WSGI Server**: Gunicorn
- **External APIs**: JSONPlaceholder

## 📋 Available Endpoints

- `/` - Home page
- `/tasks/` - Task list view
- `/tasks/new/` - Create new task
- `/tasks/<id>/update/` - Update existing task
- `/tasks/<id>/delete/` - Delete task
- `/report/` - Task reporting dashboard
- `/external-posts/` - External API integration
- `/admin/` - Django admin interface

## 🔧 Configuration

### Environment Variables

For production deployment, the following environment variables can be set:

- `DJANGO_SECRET_KEY` - Django secret key
- `DJANGO_DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection URL
- `EXTERNAL_HOSTNAME` - External hostname for CSRF trusted origins

### Local Development

The application uses SQLite for local development by default. No additional database setup is required.

## 🚀 Deployment

The application is configured for deployment on Render with:

- Automatic static file collection
- Database URL configuration
- Production-ready settings
- WhiteNoise for static file serving

## 📝 License

This project is created as part of a Django REST assignment.

## 👥 Author

Created as part of a Django REST API assignment demonstrating CRUD operations, reporting, and external API integration.
