"""Analytics module for newsletter tracking and metrics."""

from .storage import AnalyticsDB
from .dashboard import generate_report

__all__ = ["AnalyticsDB", "generate_report"]
