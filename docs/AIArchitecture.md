# AI Architecture

**Author : Mohit Singh**

AI is capability-oriented. Production asks for capabilities such as image generation, character reference, speech synthesis, vision or embeddings. The orchestrator selects a local model through an adapter.

```text
Application -> Capability -> AI Orchestrator -> Adapter -> Local Model
```

Capability areas: LLM, vision, image, video, TTS, STT, music/SFX and embeddings.

Projects reference explicit model versions. Training creates new versions; existing projects retain their approved snapshots.

The current ~8 GB VRAM target requires model loading/unloading, resource checks, caching, quantization/adapters where appropriate and careful scheduling.
