---
id: "neural-sequence-language-models"
title: "Neural sequence models, attention and language-model adaptation"
domains:
  - "language-vision-cognition"
  - "machine-learning"
  - "reinforcement-learning"
evidence_refs:
  - "in2361:sequence-models"
  - "in2361:alignment"
  - "additional-cognitive-systems:language-evaluation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "retrieval-grounded-dialogue"
  -
    type: "related_to"
    target: "text-tokenization-language-statistics"
---

# Neural sequence models, attention and language-model adaptation

## Recurrence, attention and reusable sequence state

A feedforward language model jointly learns embeddings and a fixed-window predictor. An RNN carries hidden state through shared recurrence parameters; BPTT accumulates chain-rule gradients across positions. Products of recurrent Jacobians explain vanishing/exploding gradients, not an unconditional impossibility of learning long sequences. LSTM gates regulate memory writing/retention/output; GRU is a related gated alternative. Stacking and bidirectionality change available context; bidirectional information is not available for unrestricted causal next-token prediction.

Sequence classification, token labeling and autoregressive generation need different input/output arrangements. Encoder–decoder attention computes decoder-conditioned scores over encoder states and a normalized weighted context, avoiding one fixed-dimensional source summary.

Transformers form projected queries \(Q\), keys \(K\), values \(V\):
\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}(QK^T/\sqrt{d_k})V.
\]
Here \(d_k\) is key dimension; row-normalized scores weight source values. Multi-head projections expose parallel relational subspaces. Causal masking prevents future-token leakage; positional representations address content-only permutation ambiguity. Feedforward blocks, residual additions and layer normalization complete a block. Encoder-only, decoder-only and encoder–decoder layouts serve different objectives.

## Pretraining, adaptation and generation are separate operations

Autoregressive pretraining differs from masked tokens/spans and next-sentence objectives. TagLM/ELMo/BERT illustrate recurrent/contextual and bidirectional-Transformer representations. Feature extraction freezes a representation; fine-tuning changes parameters. LoRA freezes base weights and learns a low-rank update path, without a supplied personal fine-tuning experiment.

KV caching reuses previous key/value states at generation. Greedy and beam search seek likely sequences differently; top-k, nucleus/top-p and temperature sampling control diversity. A larger beam is not automatically better translation or dialogue quality. Empirical model/data/compute scaling laws are descriptions under study conditions, not universal optimization/generalization theorems.

Machine translation adds latent word alignments, parallel/embedding-based sentence alignment, BPE/WordPiece, morphology and word-order problems, attention/cross-attention and back-translation from monolingual target data. BLEU's n-gram agreement/brevity penalty, chrF's character precision/recall, BERTScore's contextual matching and human adequacy/fluency assess different aspects.

## Instruction and preference optimization

Prompting/in-context demonstrations condition a model without necessarily training parameters. Supervised instruction fine-tuning is different. Automatic prompt search uses candidate expansion/paraphrase/truncation and evaluation; chain-of-thought demonstrations are not proof of correctness or faithful internal reasoning.

Bradley–Terry preference modeling motivates RLHF with reference-policy KL regularization and PPO. The source's malformed reward/KL display is not reconstructed. DPO instead fits preferred-versus-rejected reference-adjusted log-probability ratios through a logistic preference loss; its derivation connects reward-reweighted reference policies with preference fitting without an online RL loop. This is related to [policy optimization geometry](policy-optimization-geometry.md), not a claim that clipping guarantees alignment or safety.

## Inference engineering and evaluation limits

Cognitive Systems compares dense Transformers, sparse MoE routing/load balance and state-space sequence models at introductory depth. Quantization distinguishes post-training versus quantization-aware training, mixed precision and dynamic/static activation calibration. Its supplied notebook configures Qwen inference with 4-bit NF4, double quantization and float16 computation via Transformers/BitsAndBytes. This is teaching-code evidence, not a personally optimized deployment.

The requested HumanEval-style 50-item accuracy/latency comparison is reduced in the supplied code to five single-generation task tests, with no recorded latency study or robust pass@k estimate. Direct execution of generated code is not a security sandbox. Self-reported/scorer uncertainty, self-consistency, debate and RECSIP semantic-clustering/agreement methods can still agree on wrong answers and incur extra inference cost. Local attention/feature/example explanations and global probes/neuron/concept/mechanistic explanations also differ from faithful explanations.

[IN2361](../evidence/in2361.yaml) provides the detailed sequence/translation/alignment theory; [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) adds supplied inference/evaluation tooling. No code/API/training was executed, and neither source establishes personally completed language-model projects.
