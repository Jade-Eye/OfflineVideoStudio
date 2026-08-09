# Offline AI Video Production Studio — Master Architecture

**Author : Mohit Singh**

## Vision
A private, single-user, fully offline, open-source Windows desktop application for anime and realistic video production, using image-first scene generation, local multimodal AI, audio, sequencing, preview and final rendering up to 1080p.

## Principles
- Offline-first; no cloud dependency during normal operation.
- Single local user.
- Windows-only target.
- Python 3.11.15.
- PySide6 desktop UI.
- PostgreSQL + pgvector.
- Large media stays on the project filesystem.
- Projects live on user-selected external storage.
- Production and training are isolated.
- Model versions are explicit and reproducible.
- New ideas may evolve the architecture through review.

## Layers
UI -> Application Services -> Domain -> AI Orchestrator / Infrastructure.

Major domains: projects, stories, characters, scenes, shots, assets, production, knowledge, training, continuity, models and hardware.

## AI boundary
Application code requests capabilities through an AI orchestrator and model adapters rather than hard-coding model implementations.

## Storage boundary
PostgreSQL stores metadata, relationships, production state, model registry records, training records and embeddings. Project files store images, audio, video, documents, datasets, previews and exports.
