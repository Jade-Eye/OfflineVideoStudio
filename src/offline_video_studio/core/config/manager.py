"""
Offline AI Video Studio
Configuration Manager

Author : Mohit Singh
"""

from __future__ import annotations

from pathlib import Path

from .loader import build_config
from .models import AppConfig


class ConfigurationManager:
    """
    Central entry point for application configuration.

    The rest of the application should depend on this manager
    rather than directly reading TOML or environment variables.
    """

    def __init__(
        self,
        project_root: Path,
    ) -> None:
        self.project_root = project_root.resolve()

        self.config_directory = (
            self.project_root
            / "src"
            / "offline_video_studio"
            / "core"
            / "config"
        )

        self.defaults_path = (
            self.config_directory
            / "defaults.toml"
        )

        self.user_path = (
            self.config_directory
            / "user.toml"
        )

        self._config: AppConfig | None = None

    def load(self) -> AppConfig:
        """
        Load and validate the complete configuration.

        Configuration is cached after the first successful load.
        """

        if self._config is None:
            self._config = build_config(
                defaults_path=self.defaults_path,
                user_path=self.user_path,
            )

        return self._config

    @property
    def config(self) -> AppConfig:
        """
        Return the loaded configuration.

        Raises:
            RuntimeError:
                If configuration has not been loaded yet.
        """

        if self._config is None:
            raise RuntimeError(
                "Configuration has not been loaded. "
                "Call ConfigurationManager.load() first."
            )

        return self._config