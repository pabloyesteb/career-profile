---
id: "structured-sequence-parsing"
title: "Hidden-state decoding, grammatical parsing and structured prediction"
domains:
  - "language-vision-cognition"
  - "optimization"
  - "probability-statistics-uq"
evidence_refs:
  - "in2361:structured-inference"
status: "reviewed"
---

# Hidden-state decoding, grammatical parsing and structured prediction

## Sum over explanations or choose one?

HMMs separate hidden-state transitions from emissions with first-order/conditional-independence assumptions. Forward dynamic programming sums state paths to obtain observation likelihood; Viterbi maximizes path scores with backpointers. Supervised counts fit known labels; a local Baum–Welch implementation is not evidenced. POS and BIO entity boundaries illustrate why token features and label-transition structure supply different information.

Linear-chain CRFs instead globally normalize conditional scores built from weighted input/transition features. Likelihood training, normalization and best-path decoding use dynamic programming, but the slide recurrence missing an exponential potential is not copied as valid. Beam pruning is an approximation, not exact forward summation or exact Viterbi with another name.

## Span grammar and tree compatibility

CFGs specify terminals, nonterminals, productions and recursive constituents. Treebanks, lexical heads, coordination/subcategorization, weak versus strong equivalence and Chomsky-normal-form conversion distinguish string recognition from tree structure. CCG uses lexical types, function application and composition at the syntax/meaning interface.

CKY/CYK charts combine left/right constituents over span split points using CNF rules. Backpointers preserve alternatives; dynamic programming avoids enumerating every ambiguous tree during recognition. Neural span parsers use contextual encodings and maximize compatible labeled-span scores, not independent best spans that might form no tree. Chunking's flat BIO spans are a weaker structure. PARSEVAL measures labeled constituent agreement. The appendix's CCG supertagging and A* agenda methods require admissible bounds for optimal-search reasoning; arbitrary neural heuristics have no such blanket guarantee.

## Dependency graphs and action systems

Arc-standard parsing uses stack/buffer SHIFT, LEFT-ARC and RIGHT-ARC actions with gold/oracle supervision. Arc-eager adds REDUCE and can attach a right dependent before completing its subtree; beam search mitigates purely greedy commitment.

Graph-based parsing scores candidate arcs and finds a maximum directed rooted spanning tree. The presented procedure picks best incoming edges, detects cycles, adjusts scores, contracts recursively and expands while removing a cycle consistently. This supports nonprojective dependencies; it is not an undirected Prim/Kruskal MST. LAS/UAS score labeled/unlabeled attachments rather than constituents.

## Cross-experience reasoning

[Graph optimization](graph-greedy-matroid-optimization.md), [matching](matching-assignment-routing.md), edit-distance alignment and these parsers all exploit constrained structure, but their feasible objects and certificates differ. [Heuristic search](heuristic-adversarial-search.md) supplies another shared language for exact versus pruned search. A common transferable analytical skill is identifying whether an inference task sums probabilities, chooses a path, selects a tree or approximates a search.

[IN2361 structured-inference evidence](../evidence/in2361.yaml) preserves current HMM/CRF/constituency/dependency coverage, the source recurrence defect, and historical-only assessment boundaries. No personal parser implementation or achieved attachment score is established.
