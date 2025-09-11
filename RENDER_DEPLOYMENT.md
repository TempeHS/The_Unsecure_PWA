# Render.com Deployment Configuration for The_Unsecure_PWA

## Overview

This document describes the steps and configuration files added to prepare the Flask app for deployment on Render.com.

## Changes Made

### 1. `render.yaml`

A `render.yaml` file was added to define the Render web service. Key settings:

- **type:** web
- **name:** flask-app
- **env:** python
- **buildCommand:** `pip install -r requirements.txt`
- **startCommand:** `gunicorn main:app --bind 0.0.0.0:10000 --timeout 120 --workers 1`
- **plan:** free
- **autoDeploy:** true
- **healthCheckPath:** `/health`

This file tells Render how to build and start your app with improved timeout and health monitoring.

### 2. `Procfile`

A `Procfile` was added to specify the production start command:

```
web: gunicorn main:app --bind 0.0.0.0:10000
```

This ensures the app runs with Gunicorn, a production-grade WSGI server.

### 3. `main.py` Updates

The Flask app has been enhanced with the following changes:

#### Application Initialization

- **Database Setup:** Automatically creates `database_files/database.db` with required tables (`users` and `feedback`)
- **File Creation:** Initializes `visitor_log.txt` and `templates/partials/success_feedback.html`
- **Directory Creation:** Creates necessary directories (`database_files`, `templates/partials`)

#### Health Check Endpoint

- **Route:** `/health`
- **Purpose:** Provides a health check endpoint for Render.com monitoring
- **Response:** Returns JSON status indicating app health

#### Production Settings

- **host:** Changed to `0.0.0.0` (required for external access)
- **port:** Changed to `10000` (matches Render config)
- **debug:** Set to `False` (for production)

### 4. Database & File Management

The app now handles missing dependencies automatically:

- **SQLite Database:** Creates tables for users and feedback on first run
- **Visitor Log:** Initializes visitor counter file
- **Templates:** Creates feedback HTML template file
- **Error Prevention:** Prevents 502 errors from missing files/directories

### 5. Requirements

No changes needed; `requirements.txt` already exists with Flask and gunicorn.

## Render.com Settings

- **Service Type:** Web Service
- **Environment:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn main:app --bind 0.0.0.0:10000 --timeout 120 --workers 1`
- **Port:** 10000 (make sure this matches your Render service settings)
- **Auto Deploy:** Enabled
- **Plan:** Free (can be changed as needed)
- **Health Check:** `/health` endpoint for monitoring

## Deployment Steps

1. Push your changes to GitHub.
2. Connect your repository to Render.com.
3. Render will detect `render.yaml` and configure the service automatically.
4. Your app will be built and started using the specified commands.
5. The initialization function will create all required files and directories.

## Troubleshooting

### 502 Bad Gateway Errors

- **Fixed:** App now initializes all required files/directories automatically
- **Health Check:** Use `/health` endpoint to verify app status
- **Timeout:** Increased to 120 seconds for startup

### Missing Files

- **Database:** Automatically created with proper schema
- **Log Files:** Initialized with default values
- **Templates:** Created as empty files that get populated during use

## Notes

- If you need environment variables, add them in the Render dashboard or in `render.yaml`.
- For static files, ensure your Flask app serves them correctly.
- The app now handles missing dependencies gracefully without crashing.
- Database is SQLite-based and will persist data between deployments.

---

For more details, see the Render.com documentation: https://render.com/docs/deploy-flask
