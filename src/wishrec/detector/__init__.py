"""Five-label silence detector: frozen Qwen3-Embedding-0.6B plus a linear head."""

from .constants import LABELS, UTILITY
from .trained import TrainedDetector, load_detector

__all__ = ["LABELS", "UTILITY", "TrainedDetector", "load_detector"]
