# Database Architecture

**Author : Mohit Singh**

PostgreSQL is the structured application database. SQLAlchemy will provide ORM/data-access abstraction. pgvector will provide vector storage and similarity retrieval. Alembic is deferred until the database foundation phase.

PostgreSQL stores projects, stories, characters, scenes, shots, assets, timelines, model registry data, datasets, training runs, settings and embeddings.

The filesystem stores images, audio, video, documents, datasets, previews, renders and exports.

Asset records should use project-relative paths, for example `generated/images/scene_012/shot_004.png`, rather than hard-coded absolute paths.

pgvector is a memory/retrieval mechanism, not a replacement for neural network training.

Training flow: production data -> approval -> training candidate -> versioned dataset -> training -> evaluation -> model registry.
