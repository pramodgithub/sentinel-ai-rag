"""Metrics tracking utilities"""

import time

_metrics = {}


def record_metric(name: str, value: float):
    """Record a metric value with a timestamp."""
    _metrics[name] = (time.time(), value)


def get_metric(name: str):
    """Retrieve the latest metric value."""
    return _metrics.get(name)
