---
id: "text-tokenization-language-statistics"
title: "Text normalization, edit distance and statistical language models"
domains:
  - "language-vision-cognition"
  - "probability-statistics-uq"
evidence_refs:
  - "in2361:text-statistics"
status: "reviewed"
---

# Text normalization, edit distance and statistical language models

## From symbols to modeled units

Regular expressions supply classes, alternatives, repetition, anchors and rule-based matching; ELIZA illustrates their explanatory limits. Tokens versus vocabulary types, Unicode, punctuation, clitics, compounds and non-whitespace languages complicate preprocessing. Lemmatization differs from Porter-style suffix stemming. Sentence segmentation uses contextual classification rather than splitting every period.

BPE iteratively merges frequent adjacent symbol pairs into subword units, balancing vocabulary size against unseen-word coverage. Tokenization changes the unit of prediction and therefore the interpretation of token-normalized metrics.

Minimum edit distance uses a prefix dynamic program with insertion/deletion/substitution alternatives, initialized boundaries and alignment backpointers. The illustrated costs are insertion/deletion one, substitution two and match zero; costs belong to the application, not an immutable Levenshtein convention. Spelling correction and alignment share this structure.

## Finite context, unseen events and information rate

Sentence probability factorizes by the chain rule; n-grams approximate the conditional context by a finite history. Conditional counts yield maximum-likelihood estimates, but sparse/unseen contexts need probability allocation. Laplace/add-one, discounting, Katz backoff and interpolation trade higher-order evidence against lower-order coverage. Held-out mixture fitting and EM are discussed. Absolute discounting removes a fixed amount from seen counts; Kneser–Ney is named, not fully derived.

Stupid Backoff supplies heuristic scores, **not a normalized probability distribution**. Consequently its scores cannot simply be treated as likelihoods or perplexities. Corpus/domain and unknown-word conventions also matter.

Entropy, cross-entropy and per-token perplexity connect uncertainty with average predictive log probability. The Shannon–McMillan–Breiman statement concerns asymptotic information rates under stationary/ergodic assumptions, not a finite-sample guarantee for neural training. [Neural sequence models](neural-sequence-language-models.md) replace count contexts with learned representations but retain the need for explicit prediction units and evaluation distributions.

## Complementary statistical knowledge

NLP adds multinomial Naive Bayes bag-of-words counts, smoothed class-conditionals and log-domain scoring, plus discriminative logistic/softmax losses and lexical/negation features. Precision/recall, micro/macro F1 and ROC/AUC address different imbalance/aggregation questions. Paired bootstrap comparison resamples the **same** examples for both systems; ambiguous slide p-value wording is not promoted to a general test formula.

[IN2361 evidence](../evidence/in2361.yaml) links current slides and historical corroboration without claiming personal code or assignment completion. [Classification](generative-discriminative-classification.md) and [risk/selection](statistical-risk-model-selection.md) hold the shared model distinctions rather than duplicating their general derivations here.
