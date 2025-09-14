# Render.com Deployment Guide

## Overview

This document outlines all customizations made to The_Unsecure_PWA for deployment on render.com. The refactoring approach isolates render.com-specific changes into a separate module (`render_config.py`) to make merging from the main branch easier.

## File Structure

```
.
├── main.py                    # Minimal changes from main branch
├── render_config.py           # NEW: All render.com customizations
├── user_management.py         # No changes from main branch
├── render.yaml                # NEW: Render deployment config
├── Procfile                   # NEW: Production start command
├── deploy_script.py           # NEW: Nightly deployment automation
└── requirements.txt           # SIMPLIFIED: Reduced dependencies
```

## 1. New Files Created

### `render_config.py` (NEW)

Contains all render.com-specific functionality:

**Key Functions:**

- `setup_logging(app)` - DEBUG level logging to stdout
- `init_app(app)` - Auto-creates database, directories, and files
- `health_check()` - Health endpoint at `/health`
- `create_enhanced_route()` - Adds logging and error handling to routes
- `configure_app_for_render(app)` - Main setup function
- `get_render_run_config()` - Returns production Flask settings

**Features Added:**

- Comprehensive logging with timestamps
- Automatic database initialization (SQLite)
- Health check endpoint for monitoring
- Enhanced error handling with try/catch
- Production-ready Flask configuration

### `render.yaml` (NEW)

Render.com deployment configuration:

```yaml
services:
  - type: web
    name: flask-app
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn main:app --bind 0.0.0.0:10000 --timeout 120 --workers 1"
    plan: free
    autoDeploy: true
    healthCheckPath: "/health"
```

### `Procfile` (NEW)

Production start command:

```
web: gunicorn main:app --bind 0.0.0.0:10000
```

### `deploy_script.py` (NEW)

Automated deployment script for nightly maintenance:

**Key Functions:**

- `clear_build_cache()` - Clears Render build cache via API
- `trigger_deployment()` - Initiates fresh deployment
- `wait_for_deployment()` - Monitors deployment progress
- `get_service_info()` - Retrieves service details from Render API

**Features:**

- Comprehensive error handling and logging
- API authentication with Render.com
- Deployment status monitoring
- Timeout handling for long deployments
- Exit codes for cron job monitoring

## 2. Modified Files

### `main.py` - Minimal Changes from Main Branch

**Main Branch Version:**

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import user_management as dbHandler

app = Flask(__name__)

# Route definitions (identical)...

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=5000)
```

**Render.com Branch Version:**

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import user_management as dbHandler

# Import render.com specific configuration
import render_config                              # ADDED

app = Flask(__name__)

# Configure app for render.com deployment
render_config.configure_app_for_render(app)      # ADDED

# Route definitions (identical to main branch)...

if __name__ == "__main__":
    # Get render.com specific run configuration
    run_config = render_config.get_render_run_config()  # CHANGED
    app.run(**run_config)                               # CHANGED
```

**Summary of Changes:**

- ✅ Added `import render_config`
- ✅ Added `render_config.configure_app_for_render(app)` call
- ✅ Changed `if __name__ == "__main__":` block to use render config
- ✅ All route logic remains identical to main branch

### `user_management.py` - No Changes

This file remains identical to the main branch. No render.com-specific modifications were needed.

### `requirements.txt` - Simplified Dependencies

**Main Branch Dependencies:**

```
Flask
Flask_cors
Flask-csp
Flask-WTF
Flask-Limiter
qrcode
pyotp
bcrypt
requests
matplotlib
rich
```

**Render.com Branch Dependencies:**

```
Flask
gunicorn
```

**Summary of Changes:**

- ✅ Removed security-related packages (Flask-csp, Flask-WTF, Flask-Limiter, bcrypt)
- ✅ Removed QR code and OTP functionality (qrcode, pyotp)
- ✅ Removed visualization and request libraries (matplotlib, requests, rich)
- ✅ Removed CORS handling (Flask_cors)
- ✅ Kept only essential packages: Flask for the web framework and gunicorn for production serving

**Rationale:**
The render.com branch focuses on basic functionality demonstration and removes advanced security features and extra dependencies to simplify deployment and reduce potential conflicts.

## 3. Configuration Differences

| Setting               | Main Branch      | Render.com Branch            |
| --------------------- | ---------------- | ---------------------------- |
| **Port**              | 5000             | 10000                        |
| **Debug**             | True             | False                        |
| **Host**              | "0.0.0.0"        | "0.0.0.0" (same)             |
| **Dependencies**      | 11 packages      | 2 packages (Flask, gunicorn) |
| **Logging**           | Basic            | Comprehensive DEBUG          |
| **Database Init**     | Manual           | Automatic                    |
| **Health Check**      | None             | `/health` endpoint           |
| **Error Handling**    | Basic            | Enhanced with logging        |
| **Production Server** | Flask dev server | Gunicorn                     |

## 4. Automatic Initialization

The render.com branch automatically creates all required files and directories:

### Database Setup

- Creates `database_files/` directory
- Initializes `database_files/database.db` with tables:
  - `users` (id, username, password, dateOfBirth)
  - `feedback` (id, feedback)

### File Creation

- `visitor_log.txt` - Initialized with "0"
- `templates/partials/` directory
- `templates/partials/success_feedback.html` - Empty file

### Error Prevention

- Prevents 502 errors from missing files/directories
- Graceful handling of missing dependencies
- Comprehensive error logging

## 5. Health Monitoring

### Health Check Endpoint: `/health`

**Response Format:**

```json
{
  "status": "healthy",
  "message": "App is running",
  "database": "connected"
}
```

**Error Response:**

```json
{
  "status": "unhealthy",
  "message": "Database error: [error details]"
}
```

## 6. Enhanced Logging

All routes now include:

- Request method logging
- Endpoint access logging
- Error logging with stack traces
- Function entry/exit logging

**Log Format:**

```
2025-09-13 23:53:17,894 - main - INFO - home endpoint accessed with method: GET
2025-09-13 23:53:17,895 - main - INFO - Displaying home page with message:
```

## 7. Production Deployment

### Gunicorn Configuration

- **Workers:** 1 (free tier limit)
- **Timeout:** 120 seconds
- **Port:** 10000
- **Logging:** Debug level with access/error logs

### Auto-Deploy Settings

- Deploys automatically on git push
- Uses `render.yaml` for configuration
- Health checks ensure service availability

## 8. Merging from Main Branch

To merge changes from main branch:

1. **Easy merge** - Only 3 lines need attention in `main.py`:

   - Import statement
   - Configuration call
   - Run configuration

2. **Route changes** - Merge cleanly (identical code structure)

3. **New features** - Add normally, render config applies automatically

**Example Merge Conflict Resolution:**

```python
# Main branch adds new route
@app.route("/new-feature")
def new_feature():
    return render_template("new.html")

# Render branch: No changes needed!
# Enhanced logging/error handling applies automatically
```

## 9. Benefits

✅ **Easy Merging** - Minimal differences from main branch  
✅ **Modular Design** - All customizations isolated  
✅ **Production Ready** - Proper logging, health checks, error handling  
✅ **Auto-Setup** - No manual database/file creation needed  
✅ **Monitoring** - Health endpoint for service monitoring  
✅ **Error Recovery** - Graceful handling of missing dependencies

## 10. Render.com Dashboard Settings

When setting up the service on render.com, configure the following settings in the dashboard:

### Basic Service Configuration

| Setting            | Value            | Description                            |
| ------------------ | ---------------- | -------------------------------------- |
| **Service Type**   | Web Service      | Choose "Web Service" when creating     |
| **Repository**     | Your GitHub repo | Connect to The_Unsecure_PWA repository |
| **Branch**         | render.com       | Use the render.com branch, not main    |
| **Root Directory** | (leave blank)    | App is in root directory               |

### Build & Deploy Settings

| Setting           | Value                                                              | Description                   |
| ----------------- | ------------------------------------------------------------------ | ----------------------------- |
| **Runtime**       | Python 3                                                           | Auto-detected from repository |
| **Build Command** | `pip install -r requirements.txt`                                  | Installs Flask and gunicorn   |
| **Start Command** | `gunicorn main:app --bind 0.0.0.0:10000 --timeout 120 --workers 1` | Production server command     |

### Advanced Settings

| Setting               | Value      | Description                       |
| --------------------- | ---------- | --------------------------------- |
| **Port**              | 10000      | Must match the port in your app   |
| **Health Check Path** | `/health`  | Uses our custom health endpoint   |
| **Auto-Deploy**       | ✅ Enabled | Deploys automatically on git push |
| **Plan**              | Free       | Starter plan (can upgrade later)  |

### Optional Environment Variables

If you need to add environment variables, configure these in the "Environment" tab:

| Variable    | Value        | Purpose                                     |
| ----------- | ------------ | ------------------------------------------- |
| `FLASK_ENV` | `production` | Sets Flask environment (optional)           |
| `PORT`      | `10000`      | Backup port setting (usually auto-detected) |

### Important Notes

⚠️ **Port Configuration**: Ensure the port in render.com matches your app (10000)  
⚠️ **Branch Selection**: Deploy from `render.com` branch, not `main`  
⚠️ **Build Time**: First deployment may take 2-3 minutes  
⚠️ **Free Tier Limits**: Service sleeps after 15 minutes of inactivity

## 11. Deployment Steps

1. **Push to GitHub** - Changes auto-deploy to render.com
2. **Service Creation** - Render detects `render.yaml` automatically
3. **Build Process** - Installs dependencies via `requirements.txt`
4. **Startup** - Uses Gunicorn with optimized settings
5. **Health Check** - Monitors `/health` endpoint
6. **Ready** - App available with all features enabled

## 12. Automated Nightly Deployment

### Cron Job Configuration

A cron service has been configured to automatically clear the build cache and trigger a fresh deployment every night at midnight Australian Eastern Standard Time (AEST).

**Schedule:** `0 14 * * *` (14:00 UTC = Midnight AEST)

### Cron Service in render.yaml

```yaml
- type: cron
  name: nightly-deployment
  env: python
  schedule: "0 14 * * *" # Midnight AEST (UTC+10) = 14:00 UTC
  buildCommand: "pip install requests"
  startCommand: "python deploy_script.py"
  plan: free
```

### Required Environment Variables

The cron job requires these environment variables to be set in Render.com dashboard:

| Variable            | Description                      | Where to Find                               |
| ------------------- | -------------------------------- | ------------------------------------------- |
| `RENDER_API_KEY`    | Your Render.com API key          | Account Settings → API Keys                 |
| `RENDER_SERVICE_ID` | The service ID of your Flask app | Service Dashboard → Settings → Service Info |

### Setting Up Environment Variables

1. **Get API Key:**

   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Navigate to Account Settings → API Keys
   - Create a new API key or use existing one
   - Copy the key value

2. **Get Service ID:**

   - Go to your Flask app service in Render dashboard
   - Click on "Settings" tab
   - Find "Service Info" section
   - Copy the Service ID (starts with `srv-`)

3. **Configure Environment Variables:**
   - In your cron service dashboard
   - Go to "Environment" tab
   - Add both variables:
     ```
     RENDER_API_KEY=your_api_key_here
     RENDER_SERVICE_ID=srv-your_service_id_here
     ```

### What the Cron Job Does

1. **Cache Clearing:** Clears the build cache to ensure fresh builds
2. **Fresh Deployment:** Triggers a new deployment from the latest code
3. **Status Monitoring:** Waits for deployment completion and reports status
4. **Logging:** Provides detailed logs of the entire process

### Benefits

✅ **Automatic Updates** - Ensures your app uses the latest dependencies  
✅ **Fresh Environment** - Clears potential build artifacts and cache issues  
✅ **Scheduled Maintenance** - Runs during low-traffic hours (midnight AEST)  
✅ **Zero Downtime** - Uses Render's blue-green deployment strategy  
✅ **Monitoring** - Detailed logging of deployment process  
✅ **Error Handling** - Graceful failure handling with proper exit codes

### Monitoring the Cron Job

- **Logs:** Check the cron service logs in Render dashboard
- **Schedule:** Runs daily at midnight AEST (2:00 PM UTC)
- **Duration:** Typically completes within 5-10 minutes
- **Notifications:** Configure Render notifications for deployment status

---

This refactoring ensures the render.com branch can easily incorporate updates from the main branch while maintaining all production-ready features needed for deployment.
