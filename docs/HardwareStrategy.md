# Hardware Strategy

**Author : Mohit Singh**

Current baseline: RTX 5060 Laptop GPU, approximately 8 GB VRAM, NVIDIA driver 610.47, Windows WDDM.

Required mechanisms: model load/unload, resource checks, CPU/GPU selection, caching, safe batching, quantization where supported, adapter/LoRA customization, checkpointing and resume.

Internal SSD: application, Python environment, PostgreSQL and active cache. External HDD: production projects, large media, datasets and archives. Storage locations must be configurable.
