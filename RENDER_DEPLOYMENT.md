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
- **startCommand:** `gunicorn main:app --bind 0.0.0.0:$PORT`
- **pythonVersion:** 3.11.8
- **plan:** free
- **autoDeploy:** true

This file tells Render how to build and start your app.

### 2. `Procfile`

A `Procfile` was added to specify the production start command:

```
web: gunicorn main:app --bind 0.0.0.0:$PORT
```

This ensures the app runs with Gunicorn, a production-grade WSGI server.

### 3. `main.py` Update

The Flask app's run command was updated:

- **host:** Changed to `0.0.0.0` (required for external access)
- **port:** Uses the `PORT` environment variable provided by Render.com
- **debug:** Set to `False` (for production)

### 4. Requirements

No changes needed; `requirements.txt` already exists.

## Render.com Settings

- **Service Type:** Web Service
- **Environment:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn main:app --bind 0.0.0.0:$PORT`
- **Port:** Uses the `PORT` environment variable (no need to hardcode)
- **Python Version:** 3.11.8 (specified for compatibility)
- **Auto Deploy:** Enabled
- **Plan:** Free (can be changed as needed)

## Deployment Steps

1. Push your changes to GitHub.
2. Connect your repository to Render.com.
3. Render will detect `render.yaml` and configure the service automatically.
4. Your app will be built and started using the specified commands.

## Notes

- If you need environment variables, add them in the Render dashboard or in `render.yaml`.
- For static files, ensure your Flask app serves them correctly.
- For database connections, configure persistent storage or environment variables as needed.

---

For more details, see the Render.com documentation: https://render.com/docs/deploy-flask
