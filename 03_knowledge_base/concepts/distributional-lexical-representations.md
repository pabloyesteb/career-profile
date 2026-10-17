---
id: "distributional-lexical-representations"
title: "Distributional semantics, embeddings and affect lexicons"
domains:
  - "language-vision-cognition"
  - "machine-learning"
  - "probability-statistics-uq"
evidence_refs:
  - "in2361:lexical-representations"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "matrix-low-rank-pca"
  -
    type: "related_to"
    target: "retrieval-grounded-dialogue"
---

# Distributional semantics, embeddings and affect lexicons

## Meaning through usage and geometry

Lexical senses, synonymy, hyponymy, meronymy and antonymy distinguish similarity from relatedness and connotation. Term–document and word–context matrices represent usage rather than symbolic identity alone. TF–IDF and cosine similarity weight/compare vectors; PMI/positive PMI measures co-occurrence association but has rare-event bias, motivating context-frequency smoothing.

Skip-gram with negative sampling trains target/context vectors to discriminate observed pairs from noise pairs. Positive compatibility increases, negative compatibility decreases through stochastic logistic updates. The illustrated negative distribution is a smoothed unigram with exponent 0.75; it is a training choice, not a universal statistical constant.

Sparse counts, learned dense vectors and truncated-SVD/latent-semantic-analysis vectors optimize different representations. [SVD/PCA](matrix-low-rank-pca.md) supplies canonical matrix approximation; it does not establish that every predictive embedding is a best rank approximation. t-SNE is visualization, not the language training objective.

## Evaluating associations rather than assuming truth

Analogy tests, WordSim353, SimLex999, contextual similarity and TOEFL-style questions probe different relations. Historical semantic change and cultural/gender bias show dependence on corpus and era. These are educational evaluations, not verified personal outcomes or context-free facts about the world.

Affect adds sentiment, discrete emotions, valence–arousal–dominance and social connotation. NRC-VAD and LIWC supply different annotation/category structures. Semantic-axis induction uses positive/negative anchor directions. SentProp propagates seed polarity through a nearest-neighbor graph/random walks and repeats seed choice to estimate variability. Adjective-conjunction bootstrapping and rating-conditioned counts offer different supervision routes.

Dirichlet-prior-smoothed log odds uses background counts to shrink sparse class estimates; variance-standardized differences identify unusually associated words. That is not raw frequency subtraction or an end-to-end classifier. Personality-language/Big Five examples are model applications, not validated statements about the user's traits.

## Cross-domain interpretation

Learned vectors support [retrieval](retrieval-grounded-dialogue.md), entity matching and semantic preferences, but a high cosine match is not logical entailment or causal effect. [Information coding](information-coding-sensory-inference.md) also asks what representation preserves, under different response/noise assumptions. Biological and linguistic codes are not interchangeable training models.

[IN2361 lexical-representation claims](../evidence/in2361.yaml) preserve the source's objective/evaluation distinctions. No locally supplied implementation or personal embedding/lexicon-induction experiment is established.
