#!/usr/bin/env python3
"""
Nightly deployment script for Render.com
Clears build cache and triggers a fresh deployment at midnight AEST.
"""

import os
import sys
import time
import requests
from datetime import datetime

# Render.com API Configuration
RENDER_API_BASE = "https://api.render.com/v1"
RENDER_API_KEY = os.environ.get("RENDER_API_KEY")
SERVICE_ID = os.environ.get("RENDER_SERVICE_ID")


def log_message(message):
    """Log message with timestamp"""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{timestamp}] {message}")


def check_environment():
    """Check if required environment variables are set"""
    if not RENDER_API_KEY:
        log_message("ERROR: RENDER_API_KEY environment variable not set")
        return False

    if not SERVICE_ID:
        log_message("ERROR: RENDER_SERVICE_ID environment variable not set")
        return False

    log_message("Environment variables configured correctly")
    return True


def get_service_info():
    """Get service information from Render API"""
    try:
        headers = {
            "Authorization": f"Bearer {RENDER_API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.get(
            f"{RENDER_API_BASE}/services/{SERVICE_ID}", headers=headers, timeout=30
        )

        if response.status_code == 200:
            service = response.json()
            log_message(
                f"Service found: {service.get('name', 'Unknown')} (ID: {SERVICE_ID})"
            )
            return service
        else:
            log_message(
                f"Failed to get service info: {response.status_code} - {response.text}"
            )
            return None

    except requests.exceptions.RequestException as e:
        log_message(f"Error getting service info: {str(e)}")
        return None


def clear_build_cache():
    """Clear the build cache for the service"""
    try:
        headers = {
            "Authorization": f"Bearer {RENDER_API_KEY}",
            "Content-Type": "application/json",
        }

        # Render API endpoint for clearing cache
        response = requests.post(
            f"{RENDER_API_BASE}/services/{SERVICE_ID}/clear-cache",
            headers=headers,
            timeout=30,
        )

        if response.status_code in [200, 202]:
            log_message("✅ Build cache cleared successfully")
            return True
        else:
            log_message(
                f"❌ Failed to clear cache: {response.status_code} - {response.text}"
            )
            return False

    except requests.exceptions.RequestException as e:
        log_message(f"❌ Error clearing cache: {str(e)}")
        return False


def trigger_deployment():
    """Trigger a new deployment"""
    try:
        headers = {
            "Authorization": f"Bearer {RENDER_API_KEY}",
            "Content-Type": "application/json",
        }

        # Create a new deploy
        deploy_data = {"clearCache": "do_not_clear"}  # We already cleared it manually

        response = requests.post(
            f"{RENDER_API_BASE}/services/{SERVICE_ID}/deploys",
            headers=headers,
            json=deploy_data,
            timeout=30,
        )

        if response.status_code in [200, 201]:
            deploy = response.json()
            deploy_id = deploy.get("id", "Unknown")
            log_message(
                f"✅ Deployment triggered successfully (Deploy ID: {deploy_id})"
            )
            return deploy_id
        else:
            log_message(
                f"❌ Failed to trigger deployment: {response.status_code} - {response.text}"
            )
            return None

    except requests.exceptions.RequestException as e:
        log_message(f"❌ Error triggering deployment: {str(e)}")
        return None


def wait_for_deployment(deploy_id, max_wait_minutes=10):
    """Wait for deployment to complete"""
    if not deploy_id:
        return False

    headers = {
        "Authorization": f"Bearer {RENDER_API_KEY}",
        "Content-Type": "application/json",
    }

    max_attempts = max_wait_minutes * 2  # Check every 30 seconds

    for attempt in range(max_attempts):
        try:
            response = requests.get(
                f"{RENDER_API_BASE}/services/{SERVICE_ID}/deploys/{deploy_id}",
                headers=headers,
                timeout=30,
            )

            if response.status_code == 200:
                deploy = response.json()
                status = deploy.get("status", "unknown")

                log_message(f"Deployment status: {status}")

                if status == "live":
                    log_message("✅ Deployment completed successfully!")
                    return True
                elif status in ["build_failed", "cancelled", "deactivated"]:
                    log_message(f"❌ Deployment failed with status: {status}")
                    return False

            time.sleep(30)  # Wait 30 seconds before next check

        except requests.exceptions.RequestException as e:
            log_message(f"Error checking deployment status: {str(e)}")
            time.sleep(30)

    log_message("⚠️  Deployment status check timed out")
    return False


def main():
    """Main deployment process"""
    log_message("🚀 Starting nightly deployment process")
    log_message(f"Target: Clear cache and deploy at midnight AEST")

    # Check environment
    if not check_environment():
        log_message("❌ Environment check failed. Exiting.")
        sys.exit(1)

    # Get service info
    service = get_service_info()
    if not service:
        log_message("❌ Could not retrieve service information. Exiting.")
        sys.exit(1)

    # Clear build cache
    log_message("🧹 Clearing build cache...")
    cache_cleared = clear_build_cache()

    if cache_cleared:
        # Wait a moment for cache clear to process
        log_message("⏳ Waiting for cache clear to process...")
        time.sleep(10)

        # Trigger deployment
        log_message("🚀 Triggering fresh deployment...")
        deploy_id = trigger_deployment()

        if deploy_id:
            # Wait for deployment to complete
            log_message("⏳ Waiting for deployment to complete...")
            success = wait_for_deployment(deploy_id, max_wait_minutes=10)

            if success:
                log_message("🎉 Nightly deployment completed successfully!")
                sys.exit(0)
            else:
                log_message("❌ Deployment did not complete successfully")
                sys.exit(1)
        else:
            log_message("❌ Failed to trigger deployment")
            sys.exit(1)
    else:
        log_message("❌ Failed to clear build cache. Skipping deployment.")
        sys.exit(1)


if __name__ == "__main__":
    main()
