# Training Architecture

**Author : Mohit Singh**

Training is an independent studio. Active production model snapshots must never be silently modified by training.

```text
Data -> Approval -> Candidate -> Dataset Version -> Training -> Checkpoint -> Evaluation -> Model Registry -> Promotion
```

Potential training categories include story/narrative, character identity, visual style, image generation, voice/audio and other multimodal capabilities. Document retrieval and neural training remain separate concepts.

Only approved and curated production data becomes a training candidate; raw generated content is not automatically treated as training truth.
