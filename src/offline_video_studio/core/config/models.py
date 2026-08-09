"""
Offline AI Video Studio
Configuration Models

Author : Mohit Singh
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ApplicationConfig:
    """
    General application metadata and runtime environment.
    """

    name: str
    version: str
    environment: str


@dataclass(frozen=True)
class VideoConfig:
    """
    Global video-production constraints.

    The maximum resolution is deliberately restricted to 1080p.
    """

    max_width: int
    max_height: int
    default_width: int
    default_height: int
    default_fps: int


@dataclass(frozen=True)
class StorageConfig:
    """
    Global storage locations.

    These are application-level defaults. Individual projects
    will later have their own project root.
    """

    projects_directory: Path | None
    models_directory: Path | None
    datasets_directory: Path | None
    cache_directory: Path | None


@dataclass(frozen=True)
class UIConfig:
    """
    Global user-interface preferences.
    """

    theme: str
    language: str


@dataclass(frozen=True)
class HardwareConfig:
    """
    Hardware execution preferences.

    These values do not perform hardware detection yet.
    Hardware detection belongs to a later Phase 1 step.
    """

    gpu_enabled: bool
    cpu_enabled: bool
    max_gpu_memory_percent: int


@dataclass(frozen=True)
class AppConfig:
    """
    Root configuration object.

    Other application modules should receive this object instead
    of reading environment variables or configuration files directly.
    """

    application: ApplicationConfig
    video: VideoConfig
    storage: StorageConfig
    ui: UIConfig
    hardware: HardwareConfig