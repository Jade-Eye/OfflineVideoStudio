# Project Structure

**Author : Mohit Singh**

## Repository

```text
OfflineVideoStudio/
├── docs/
├── src/offline_video_studio/
├── projects/
├── models/
├── datasets/
├── cache/
├── tests/
├── scripts/
├── experiments/
├── logs/
└── installer/
```

## Source modules

```text
app/ core/ database/ domain/ studios/ ai/ production/ training/ continuity/ media/ hardware/ ui/
```

`domain` describes system concepts; `studios` contains user workspaces; `ai` contains AI integration; `production` contains the filmmaking pipeline; `training` contains learning workflows; `continuity` protects consistency; `ui` contains presentation.

Alembic is intentionally deferred until the database foundation phase.
