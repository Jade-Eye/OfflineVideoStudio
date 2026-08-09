"""
Offline AI Video Studio
Configuration Loader

Author : Mohit Singh
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import tomllib

from .models import (
    AppConfig,
    ApplicationConfig,
    HardwareConfig,
    StorageConfig,
    UIConfig,
    VideoConfig,
)


class ConfigurationError(Exception):
    """
    Raised when application configuration is invalid.
    """


def _load_toml(path: Path) -> dict[str, Any]:
    """
    Load a TOML configuration file.

    Missing files are treated as empty configuration so that
    optional user configuration can safely be absent.
    """

    if not path.exists():
        return {}

    try:
        with path.open("rb") as file:
            return tomllib.load(file)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigurationError(
            f"Invalid TOML configuration: {path}"
        ) from exc


def _merge_dicts(
    base: dict[str, Any],
    override: dict[str, Any],
) -> dict[str, Any]:
    """
    Recursively merge configuration dictionaries.

    Values from `override` take precedence over `base`.
    """

    result = dict(base)

    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = _merge_dicts(result[key], value)
        else:
            result[key] = value

    return result


def _parse_optional_path(value: str | None) -> Path | None:
    """
    Convert a configured filesystem path into a Path object.

    Empty paths are represented as None.
    """

    if not value:
        return None

    return Path(value).expanduser().resolve()


def _validate_positive_integer(
    value: Any,
    name: str,
) -> int:
    """
    Validate that a configuration value is a positive integer.
    """

    if not isinstance(value, int) or isinstance(value, bool):
        raise ConfigurationError(
            f"{name} must be an integer."
        )

    if value <= 0:
        raise ConfigurationError(
            f"{name} must be greater than zero."
        )

    return value


def _validate_percentage(
    value: Any,
    name: str,
) -> int:
    """
    Validate a percentage between 1 and 100.
    """

    value = _validate_positive_integer(value, name)

    if value > 100:
        raise ConfigurationError(
            f"{name} must be between 1 and 100."
        )

    return value


def build_config(
    defaults_path: Path,
    user_path: Path,
) -> AppConfig:
    """
    Build the final validated configuration.

    Precedence:

        defaults.toml
            ↓
        user.toml
            ↓
        environment variables
    """

    defaults = _load_toml(defaults_path)
    user = _load_toml(user_path)

    merged = _merge_dicts(defaults, user)

    application = merged.get("application", {})
    video = merged.get("video", {})
    storage = merged.get("storage", {})
    ui = merged.get("ui", {})
    hardware = merged.get("hardware", {})

    # --------------------------------------------------------
    # Environment override
    # --------------------------------------------------------

    environment = os.getenv(
        "OFFLINE_VIDEO_STUDIO_ENV",
        application.get("environment", "development"),
    )

    # --------------------------------------------------------
    # Application
    # --------------------------------------------------------

    app_config = ApplicationConfig(
        name=str(application.get(
            "name",
            "Offline AI Video Studio",
        )),
        version=str(application.get(
            "version",
            "0.1.0",
        )),
        environment=str(environment),
    )

    # --------------------------------------------------------
    # Video
    # --------------------------------------------------------

    max_width = _validate_positive_integer(
        video.get("max_width", 1920),
        "video.max_width",
    )

    max_height = _validate_positive_integer(
        video.get("max_height", 1080),
        "video.max_height",
    )

    default_width = _validate_positive_integer(
        video.get("default_width", 1920),
        "video.default_width",
    )

    default_height = _validate_positive_integer(
        video.get("default_height", 1080),
        "video.default_height",
    )

    default_fps = _validate_positive_integer(
        video.get("default_fps", 24),
        "video.default_fps",
    )

    if default_width > max_width:
        raise ConfigurationError(
            "video.default_width cannot exceed video.max_width."
        )

    if default_height > max_height:
        raise ConfigurationError(
            "video.default_height cannot exceed video.max_height."
        )

    video_config = VideoConfig(
        max_width=max_width,
        max_height=max_height,
        default_width=default_width,
        default_height=default_height,
        default_fps=default_fps,
    )

    # --------------------------------------------------------
    # Storage
    # --------------------------------------------------------

    storage_config = StorageConfig(
        projects_directory=_parse_optional_path(
            storage.get("projects_directory")
        ),
        models_directory=_parse_optional_path(
            storage.get("models_directory")
        ),
        datasets_directory=_parse_optional_path(
            storage.get("datasets_directory")
        ),
        cache_directory=_parse_optional_path(
            storage.get("cache_directory")
        ),
    )

    # --------------------------------------------------------
    # UI
    # --------------------------------------------------------

    ui_config = UIConfig(
        theme=str(ui.get("theme", "dark")),
        language=str(ui.get("language", "en")),
    )

    # --------------------------------------------------------
    # Hardware
    # --------------------------------------------------------

    max_gpu_memory_percent = _validate_percentage(
        hardware.get("max_gpu_memory_percent", 90),
        "hardware.max_gpu_memory_percent",
    )

    hardware_config = HardwareConfig(
        gpu_enabled=bool(
            hardware.get("gpu_enabled", True)
        ),
        cpu_enabled=bool(
            hardware.get("cpu_enabled", True)
        ),
        max_gpu_memory_percent=max_gpu_memory_percent,
    )

    return AppConfig(
        application=app_config,
        video=video_config,
        storage=storage_config,
        ui=ui_config,
        hardware=hardware_config,
    )