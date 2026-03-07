"""Utility to restart services or processes"""

import subprocess


def restart_service(service_name: str):
    """Restart a system service using systemctl or equivalent."""
    try:
        subprocess.run(["systemctl", "restart", service_name], check=True)
    except Exception as e:
        raise RuntimeError(f"Failed to restart {service_name}: {e}")
