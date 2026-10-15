# Natural Language Processing

## Module metadata and identity

| Field | Value |
|---|---|
| Course ID | in2361 |
| Official module code | IN2361 |
| Official course name | Natural Language Processing |
| ECTS | 6 |
| Grade | 2.7 |
| Academic record | Degree course; transcript PDF p. 3 |
| Profile status | complete_validated |

## Evidence base and material structure

Primary source: `00_sources/tum/archives/Natural Languag 950767586 (W24_25)_20261012_1553.zip`. References below identify ZIP members; page numbers are physical PDF pages, not chapter numbers printed on slides.

The archive contains 78 PDFs / 2,644 physical pages. The **24 decks / 888 pages** under `PDFs of Slides/Current WS 24-25 slides/` establish the current syllabus. Older slide folders, an old exam fact sheet, mock examination/solution and two historical examinations provide complementary evidence, not an interchangeable current syllabus. There are no local programming assignments, notebooks or implementations. All current decks were inspected through searchable text and their full page/section structure; 32 mathematical, algorithmic and diagram pages were rendered selectively. Repeated examples and progressive reveals were consolidated.

The source register assigns short identifiers to exact filenames in the current folder. An initial deck and a numbered 16 deck are not present; these numbering gaps do not establish which additional teaching content, if any, is missing. Internal chapter numbers sometimes differ from filenames. Older-only word-sense and text-to-image decks were not silently imported into the current syllabus.

## Technical content

### Text representation, regular expressions, and string algorithms

*Evidence: [S2], especially pp. 15–44; minimum-edit-distance formulation pp. 36–41.*

- Regular-expression operators, character classes, negation, alternatives, repetition and anchored patterns; rule-based conversational matching through ELIZA examples. Distinguish corpus word tokens from vocabulary types and language-dependent normalization decisions.
- Tokenization across punctuation, clitics, compounds and languages without whitespace-delimited words; Unicode and multilingual text. **Byte-pair encoding (BPE)** constructs subword units by iteratively merging frequent adjacent symbol pairs, balancing vocabulary size and representation of unseen words.
- Normalization, lemmatization and **Porter-style stemming** distinguish morphological canonicalization from suffix heuristics. Sentence segmentation is a classification problem rather than indiscriminate splitting at every period; decision-tree features encode punctuation context.
- **Levenshtein/minimum edit distance:** dynamic programming over prefixes, insertion/deletion/substitution costs, boundary initialization and backpointers for alignment. The illustrated setting charges insertion/deletion one and substitution two, with zero-cost matches; costs are modeling choices, not an invariant definition. Alignment and spelling correction illustrate the same recurrence.

### Probabilistic language modeling and information measures

*Evidence: [S3], pp. 2–27; historical mock examination [E1–E2] corroborates n-gram computation.*

- Chain-rule sentence probabilities and finite-context **n-gram Markov approximations**; maximum-likelihood conditional count estimates, sparse contexts, unknown words, corpus/domain dependence and the distinction between training fit and held-out behavior.
- **Laplace/add-one smoothing**, discounting and redistribution of probability mass; **Katz backoff**, interpolated higher/lower-order models, held-out estimation of mixture weights and the slide's EM discussion. **Absolute discounting** subtracts a fixed amount from observed counts and redistributes mass to unseen continuations. **Kneser–Ney** is recommended by name rather than derived in full.
- **Stupid Backoff** is distinguished from normalized probabilistic smoothing: its heuristic scores are not themselves a normalized distribution. Do not interpret every language-model scoring method as a probability model.
- Entropy, cross-entropy and per-token **perplexity** relate predictive log likelihood to uncertainty. The **Shannon–McMillan–Breiman theorem** motivates asymptotic sequence information rates under stationary/ergodic assumptions; it is not a finite-sample or universal convergence guarantee for trained neural models.

### Text classification, estimation, and evaluation

*Evidence: [S4], pp. 2–29; [S5], pp. 2–15.*

- **Multinomial Naive Bayes:** generative class priors and class-conditional word probabilities, conditional independence/bag-of-words assumptions, log-domain scoring, supervised count estimation and smoothed estimates. Sentiment examples cover polarity, negation handling, stopwords and unseen vocabulary.
- **Binary logistic regression** and multiclass **softmax regression** model conditional class probabilities directly. Cross-entropy training, gradients, stochastic gradient descent and L1/L2 regularization contrast discriminative estimation with Naive Bayes. Feature construction includes sentiment-bearing words, negation and punctuation/context cues.
- Confusion matrices, precision/recall, micro/macro aggregation, F1, ROC curves and AUC; class imbalance and the choice of aggregation change interpretation. **Paired bootstrap resampling** compares systems on the same resampled examples rather than treating their predictions as independent. A t-test appendix provides additional statistical context; the profile does not adopt the slide's ambiguous bootstrap p-value wording as a general formula.
- Information gain and Gini impurity appear as feature/decision-selection criteria. Evaluation separates intrinsic prediction metrics from downstream application performance.

### Distributional semantics and learned word representations

*Evidence: [S6], pp. 2–45; PCA/SVD appendix pp. 38–42.*

- Lexical meaning: senses, synonymy, hyponymy, meronymy, antonymy, similarity versus relatedness, semantic frames and connotation. Distributional representations use term–document and word–context matrices rather than symbolic word identity alone.
- **TF–IDF**, cosine similarity, **PMI/positive PMI**, rare-event bias and context-frequency smoothing. Sparse count representations and dense learned embeddings encode different statistical objectives.
- **Skip-gram with negative sampling:** target/context vectors are trained by binary logistic discrimination between observed word–context pairs and noise pairs. Negative sampling uses a smoothed unigram distribution, illustrated with exponent 0.75; stochastic gradient updates increase positive-pair compatibility and decrease negative-pair compatibility.
- **PCA**, truncated **SVD**, **latent semantic analysis/indexing** and low-rank approximation provide a complementary matrix-factorization route to distributional vectors. t-SNE is used for visualization, not as the language-model training objective.
- Analogy tests, WordSim353, SimLex999, contextual similarity and TOEFL-style questions illustrate intrinsic evaluation. Historical semantic change and cultural/gender bias show that corpus-derived representations encode social and temporal associations, not context-free truth.

### Neural language models and recurrent sequence architectures

*Evidence: [S7], pp. 2–17; [S8], pp. 2–64, particularly pp. 28–39 and 41–61.*

- Feedforward neural language models learn word embeddings jointly with a fixed-window predictor; affine layers, nonlinearities, softmax and cross-entropy are expressed as computational graphs. **Backpropagation** applies the chain rule and SGD to shared model parameters.
- **Recurrent neural networks** carry a hidden state across input positions; **backpropagation through time** accumulates gradients through repeated applications of shared recurrence parameters. Sequence classification, token labeling and autoregressive generation require different input/output arrangements; stacked and bidirectional networks increase representational scope.
- Products of recurrent Jacobians explain **vanishing/exploding gradients** and long-dependency difficulties. **LSTM** gates regulate cell-memory writing, retention and output; **GRU** gates provide a related recurrent alternative. These are architecture/mechanism explanations, not unconditional convergence theorems.
- **Encoder–decoder/sequence-to-sequence** models map a source sequence into a target sequence. Attention avoids forcing all source information through a single fixed-dimensional summary: decoder-conditioned scores over encoder states are normalized, then used to form a weighted context. The recurrent attention diagrams were inspected visually to preserve which state supplies queries and which sequence supplies values.

### Transformers, pretraining, and generation

*Evidence: [S9], pp. 2–34; [S10], pp. 2–26; [S11], pp. 2–47.*

- **Scaled dot-product attention** forms learned queries, keys and values, normalizes query–key scores scaled by the square root of key dimension, and aggregates values. **Multi-head attention** runs separate projections and combines head outputs. Causal masking prevents future-token leakage in autoregressive decoding.
- Transformer blocks combine attention, position-wise feedforward transformations, residual connections and layer normalization. Positional representations address the inability of content-only attention to distinguish arbitrary input permutations. Encoder-only, decoder-only and encoder–decoder structures serve different prediction tasks.
- Autoregressive language-model pretraining, corpus preparation and model/data/compute scaling. The presented **power-law scaling relationships** are empirical descriptions, not universal optimization or generalization guarantees. **KV caching** reuses previously computed key/value states during generation.
- **Greedy decoding**, **beam search**, **top-k sampling**, **nucleus/top-p sampling** and **temperature** expose the distinction between high-probability sequence search and stochastic diversity. Beam width and local decisions affect decoded outputs; larger search is not automatically better task performance.
- Fine-tuning versus feature extraction; **LoRA** freezes a base weight matrix and trains a low-rank update, illustrated as an additional low-rank input-to-output path. No local LoRA implementation or fine-tuning experiment is supplied.
- **Masked language modeling**, masked spans and next-sentence objectives; contextual word meaning and word-sense discrimination through contextual similarity. Fine-tuning supports single/pair classification, BIO sequence labeling and answer-span prediction.
- **TagLM**, **ELMo** and **BERT** document the transition from contextual recurrent representations to bidirectional Transformer encoders. ELMo combines representations from bidirectional language-model layers; BERT's contextual encodings can be used as features or adapted end-to-end.
- Training corpora, social bias and generated harms constrain how model behavior is evaluated and deployed.

### Instruction following, prompting, and preference alignment

*Evidence: [S12], pp. 10–43, especially pp. 24–29 and 33–37.*

- Zero-shot and few-shot prompting, in-context demonstrations and **supervised instruction fine-tuning** distinguish use-time conditioning from parameter training. **Chain-of-thought prompting** supplies intermediate reasoning demonstrations; it is not a proof of generated answer correctness.
- **Automatic prompt optimization** searches candidate prompts through expansion, paraphrase, truncation/continuation and performance evaluation. MMLU illustrates multi-domain assessment; an incomplete slide does not support a fuller missing discussion.
- Human preference pairs and a **Bradley–Terry reward model** motivate **RLHF**. Reward optimization is regularized toward a reference policy through a KL-related penalty; **PPO** is named as a policy-optimization route. The reward/KL display on p. 35 is malformed, so an exact objective is not transcribed from it.
- **Direct Preference Optimization (DPO)** uses the reference-adjusted log-probability ratio between preferred and rejected responses in a logistic preference loss. Its derivation relates an exponentially reward-reweighted reference policy to pairwise preference fitting, without a separate online RL loop. This does not imply convergence to universally aligned behavior; no such guarantee is supplied.

### Machine translation

*Evidence: [S13], pp. 2–51, especially pp. 18–21, 23–38 and 39–48.*

- Conditional translation probabilities, latent word alignments and statistical versus neural translation frameworks. Word-order differences, morphological fusion/agglutination and omitted pronouns complicate one-to-one word substitution.
- Parallel-corpus preparation, subword units (**BPE/WordPiece**) and sentence alignment using embedding similarity. Recurrent encoder–decoders with attention and Transformer cross-attention condition generation on the source sentence; beam search maintains competing partial translations.
- **Back-translation** creates synthetic parallel examples from monolingual target text. Multilingual modeling and low-resource translation expose data imbalance and transfer opportunities; examples are not evidence of a locally completed implementation.
- **BLEU** combines n-gram agreement with a brevity penalty; **chrF** evaluates character n-gram precision/recall; **BERTScore** matches contextual token representations. Human assessment distinguishes adequacy/faithfulness from fluency. Metrics and low-resource/social bias must be considered together rather than equating one score with translation quality.

### Information retrieval, question answering, and RAG

*Evidence: [S14], pp. 2–24; visual inspection pp. 6 and 12.*

- Sparse lexical retrieval through TF–IDF/cosine similarity, **BM25** term-frequency saturation and document-length normalization, and inverted indexes. Ranked evaluation includes precision/recall, average precision/MAP and reciprocal-rank measures.
- Dense embedding retrieval versus **cross-encoder reranking** of query–document pairs. **ColBERT** introduces token-level late interaction rather than collapsing both texts into a single independent vector similarity.
- **Retrieval-augmented generation (RAG)** conditions answers on retrieved passages; retrieval and answer generation are distinct failure points. Multi-hop retrieval, context selection, privacy/copyright concerns and use of external search/API sources are discussed, not implemented locally.
- Natural Questions, TyDi and multi-domain QA benchmarks illustrate task diversity. Exact/free-form answer matching, token F1 and retrieval ranking metrics evaluate different components and should not be conflated.

### Dialogue and conversational systems

*Evidence: [S15], pp. 2–42, especially pp. 7–15 and 21–39.*

- Pattern-based ELIZA, retrieval-based responses and generative chatbots; discourse mechanisms include turn taking, endpoint detection, speech acts, grounding, adjacency pairs, repair, initiative and conversational implicature.
- Task-oriented dialogue uses **frames/slots**, intent or user-act recognition, sequence tagging, dialogue-state tracking and a policy selecting system actions. Confidence-sensitive confirmation/rejection handles uncertain interpretation. **Reinforcement-learning dialogue policies** are introduced at architecture level.
- Natural-language generation separates content planning from realization. Open-domain dialogue uses conversation pretraining and retrieval/search conditioning; evaluation includes human pairwise conversation judgments (**ACUTE-Eval**), **Wizard-of-Oz** studies and iterative user-centered design.

### Sequence labeling and hidden-state inference

*Evidence: [S17], pp. 2–33; [SH], pp. 2–36; mock HMM tasks [E1–E2].*

- Part-of-speech tagging, Penn Treebank tags and named-entity recognition; **BIO** boundaries encode multi-token entity spans. Word/context features and label transitions supply different information.
- **Hidden Markov models** distinguish state transitions from emissions, make first-order state/observation independence assumptions and use supervised count estimates where labels are known. **Forward dynamic programming** sums over state paths for observation likelihood; **Viterbi decoding** maximizes over paths and retains backpointers. Beam pruning approximates exhaustive candidate retention.
- **Linear-chain conditional random fields** model a globally normalized conditional distribution using sums of weighted input/transition features. Training maximizes conditional likelihood; dynamic programming supports normalization and best-sequence inference. The CRF distribution on S17 p. 23 is clear, whereas its p. 29 recurrence omits an exponential potential; the inconsistent printed recurrence is not reproduced as correct.
- These sources support sequence modeling and inference; they do not establish a local unsupervised Baum–Welch implementation.

### Constituency syntax and chart parsing

*Evidence: [S18], pp. 2–63; pp. 49–63 explicitly form an appendix beyond the exam-relevant core.*

- **Context-free grammars**, terminals/nonterminals, productions, phrase structure, subcategorization, coordination, treebanks and lexical heads. Distinguish weak versus strong grammar equivalence and conversion to **Chomsky normal form**.
- **Combinatory categorial grammar (CCG)** uses typed lexical categories, function application and composition to combine syntax/semantic interfaces.
- **CYK/CKY parsing:** a triangular span chart combines left/right constituents over possible split positions using CNF productions. Backpointers recover trees/packed alternatives; dynamic programming avoids enumerating every ambiguous tree during recognition.
- **Neural span-based constituency parsing** scores labeled spans from recurrent/Transformer contextual encodings and maximizes a sum over valid trees. A CKY-style recurrence enforces tree compatibility; independently selecting high-scoring spans can create invalid structures.
- **PARSEVAL** evaluates labeled constituent agreement. **Chunking** predicts flatter, nonoverlapping BIO spans and is not equivalent to full recursive parsing.
- The appendix introduces CCG supertagging, sequence-model alternatives and **A\*** agenda search. Admissible heuristic bounds underpin optimal-search reasoning; the discussion is not an unconditional claim for arbitrary neural heuristics or every parser implementation.

### Dependency syntax and structured prediction

*Evidence: [S19], pp. 2–34; algorithm diagrams pp. 26–28.*

- Head–dependent relations, dependency trees, projectivity and dependency treebanks distinguish graph structure from constituency nesting.
- **Arc-standard transition parsing** uses a stack/buffer and SHIFT, LEFT-ARC and RIGHT-ARC operations. Gold/oracle configurations supervise a classifier over parser actions. **Arc-eager parsing** adds REDUCE and attaches right dependents before completing their subtrees; beam search reduces purely greedy commitment.
- **Graph-based maximum directed spanning-tree parsing** scores possible dependency edges and seeks the highest-scoring rooted tree. The presented cycle-contraction procedure selects best incoming edges, detects cycles, adjusts scores, contracts recursively and expands while breaking the cycle consistently. This supports nonprojective structures, unlike imposing projectivity by construction.
- Feature-based/neural arc scoring and labeled/unlabeled attachment scores (**LAS/UAS**) connect structured prediction to evaluation.

### Logical meaning representations

*Evidence: [SL], pp. 2–27, especially pp. 6–12 and 17–24.*

- Meaning representations are evaluated by verifiability, expressiveness, unambiguity, flexibility and their treatment of vagueness. **Model-theoretic semantics** interprets expressions over domains and denotations.
- **First-order logic** represents predicates, variables, quantification and relations; distinguish semantic entailment from syntactic proof. **Modus ponens**, forward/backward chaining and resolution illustrate inference. Soundness, completeness and undecidability delimit possible inference procedures; brief slides do not justify conflating general satisfiability decision with a terminating complete prover.
- Higher-order/modal formalisms are introduced briefly. **Neo-Davidsonian event semantics** separates an event variable from its participants/roles and supports modifiers without fixed predicate arity.
- Temporal points/intervals and **Reichenbach's speech, event and reference times** distinguish tense/aspect interpretations.
- **Description logics:** TBox concepts/role axioms versus ABox individuals/assertions; subsumption, disjointness, coverage and instance checking. **OWL**, **RDF** and Semantic Web knowledge representations connect these formalisms to machine-readable knowledge bases.

### Relation, event, and temporal information extraction

*Evidence: [S20], pp. 2–43, particularly pp. 9–22 and 25–40.*

- Entity/relation/event templates structure information extracted from text. **Hearst patterns** provide high-precision, limited-recall relation rules; supervised pipelines use lexical, dependency and contextual neural features.
- **Seed-based bootstrapping** alternates extracting tuples and learning patterns with confidence thresholds; semantic drift and error propagation are risks. **Distant supervision** aligns text with knowledge-base facts to obtain noisy training labels, not perfectly observed relation truth.
- **ReVerb/open information extraction** uses POS/phrase patterns, neighboring noun phrases and a confidence classifier to extract relations without a fixed manually enumerated relation inventory. Precision/recall evaluation depends on what constitutes a correct extraction.
- Event triggers, actions/states, tense and aspect; **Allen's interval algebra** describes relative temporal relations, while Reichenbach's representation distinguishes reference and speech times.
- **TimeML/TimeBank** annotate EVENT, TIME and temporal/aspectual/subordination links (TLINK, ALINK, SLINK). Temporal-expression recognition uses rules or sequence models; normalization combines ISO-style representations, temporal arithmetic and contextual reference dates. Extracted relations produce partial temporal orderings rather than necessarily a single exact timeline.

### Semantic roles, frames, and selectional preferences

*Evidence: [S21], pp. 2–31, especially pp. 11–16 and 20–28.*

- Thematic roles, diathesis alternations and proto-agent/proto-patient properties distinguish semantic participation from surface subject/object position.
- **PropBank** predicate-specific numbered arguments and adjunct labels versus **FrameNet** frame/role inventories. Semantic-role labeling includes candidate pruning, argument identification, role classification and global structural constraints; neural sequence labeling provides an alternative pipeline.
- **WordNet synsets** support semantic classes and selectional restrictions. **Resnik's selectional preference** quantifies the divergence between verb-conditioned semantic-class probabilities and a background class distribution through KL divergence; class-specific contributions describe association strength.
- Conditional noun/verb/argument relations and evaluation through pseudoword discrimination or human plausibility judgments tie the formal preference model to linguistic evidence.

### Affect, connotation, and lexicon induction

*Evidence: [S22], pp. 2–34, especially pp. 9–23.*

- Sentiment, discrete emotion categories, **valence–arousal–dominance (VAD)** and social connotation are distinct representation choices. NRC-VAD and **LIWC** exemplify lexicons with different annotation/category structures.
- **Semantic-axis induction** measures words relative to embedding directions defined by positive/negative anchors. **SentProp** builds a nearest-neighbor word graph, propagates seed polarity through random walks and repeats seed selection to estimate variability/confidence.
- Adjective-conjunction patterns and graph bootstrapping induce polarity without labeling every word. Review-rating-conditioned counts supply a supervised lexicon route.
- **Dirichlet-prior-smoothed log odds** uses background counts to shrink sparse class-specific estimates; variance-standardized differences identify disproportionately associated words. This differs from raw frequency differences and from training an end-to-end sentiment classifier.
- Lexicon features support sentiment and personality-language analyses; Big Five and VAD regression are application examples, not validated claims about the user's traits or a locally implemented psychological assessment.

### Coreference, entity linking, and knowledge access

*Evidence: [S23], pp. 2–51, especially pp. 18–40 and 44–48.*

- Mentions versus discourse entities; anaphora, cataphora, zero reference, discourse givenness/definiteness and nonreferential expletives constrain candidate interpretation.
- Pairwise mention classifiers and transitive closure produce clusters but can propagate a single erroneous link. **Mention-ranking models** include a no-antecedent option, contrasting with independent pair decisions and entity-level approaches.
- **End-to-end span coreference:** contextual span endpoints, attention-based soft heads and width features generate mention representations; mention and antecedent scores combine into antecedent probabilities. Marginalization over valid antecedents handles latent choices, while span pruning controls candidate growth.
- **TAGME** entity linking uses anchor/mention priors and coherence between linked entities. **ELQ** jointly detects spans and scores entity candidates through contextual mention and entity-title/text representations.
- **B-cubed** averages mention-level cluster precision/recall, unlike treating every entity cluster as a flat classification label. Gender bias is explicitly considered in coreference evaluation.
- RDF, SQL/SPARQL and semantic question answering connect entity identification to structured knowledge access; their presence does not demonstrate a completed database implementation.

### Discourse coherence and argument structure

*Evidence: [S24], pp. 2–25, especially pp. 5–21.*

- Local/global coherence, **Rhetorical Structure Theory (RST)** elementary discourse units, nucleus/satellite relations and discourse trees; **Penn Discourse Treebank** explicit/implicit relations between arguments provide a complementary annotation framework.
- Neural EDU segmentation and shift–reduce discourse parsing use contextual encoders, pooled unit/subtree representations and action classifiers; nuclearity choices distinguish NN, NS and SN combinations.
- **Centering theory** tracks backward-looking, forward-looking and preferred centers, ranking Continue, Retain, Smooth Shift and Rough Shift transitions. **Entity-grid models** encode entity occurrences as subject, object, other or absent and learn sentence-transition features.
- Self-supervised coherence objectives compare natural discourse with sentence permutations/negative examples. **Argument mining** separates claims, premises and nonargumentative content and identifies support/attack relations; persuasion features and scientific-discourse examples broaden the application beyond sentence-level syntax.

## Computational tools, applications, and evidence limits

The material is conceptual/algorithmic rather than a supplied software lab. Named model families and resources include Transformers/BERT/ELMo, LoRA, RAG, WordNet, FrameNet, PropBank, TimeML, RDF/OWL and SPARQL. They are not evidence of programming-language proficiency or implemented systems. Applications include sentiment classification, translation, search/QA, conversational agents, tagging/parsing, knowledge extraction, event timelines, affect lexicons, entity linking and discourse/argument analysis.

Historical assessments check calculation and architectural reasoning: BPE/n-grams, HMM/Viterbi, chart/CCG parsing, dependency trees, sentiment/embedding methods and neural sequence architectures. Their additional historical-only topics are not presented as established current taught content. No implementation outputs, project completion or personal quantitative performance can be inferred from exam papers.

## Coverage validation and source limitations

- All 24 current decks are represented: text/statistical modeling (S2–S6), neural/LLM sequence (S7–S15), sequence/syntax (SH, S17–S19), formal meaning/information extraction/roles (SL, S20–S21) and affect/coreference/discourse (S22–S24). Late-course topics were checked rather than inferred from the title.
- The 32 rendered pages cover edit-distance tables, smoothing/entropy, HMM inference, LSTM/attention, Transformer heads, LoRA/scaling, RLHF/DPO, CRFs, chart/A* and dependency algorithms, semantic-role/affect formulas, coreference/entity linking, retrieval and discourse structures.
- Text is selectable but can flatten subscripts, sums, matrix layouts and graph structure. Visual inspection recovered substantial missing relationships; it also confirmed source defects rather than automatically correcting them from general knowledge. Notable unresolved displays are S12 p. 35 (reward/KL objective), S17 p. 29 (CRF recurrence) and the incomplete S12 p. 32. Supported concepts are retained without endorsing those displays.
- Current-folder provenance is prioritized over older WS22/23/24 duplicates and historical exam dates. No current syllabus/fact sheet, introductory deck, practical assignments or solutions to current coursework are supplied. These gaps limit exact session-delivery and implementation claims, not the documented current slide coverage.

## Thematic categories

- Machine learning and artificial intelligence.
- Natural language processing and computational linguistics.
- Statistics, probabilistic modeling, and information theory.
- Optimization and structured prediction.
- Data science, information retrieval, and knowledge representation.

## Source register

All S identifiers below resolve under archive member directory `PDFs of Slides/Current WS 24-25 slides/`.

| ID | Exact filename | Pages |
|---|---|---:|
| S2 | `2_RegExs_TextNormalization_EditDistance.pdf` | 44 |
| S3 | `3_LanguageModellingWithNGrams.pdf` | 27 |
| S4 | `4_NaiveBayesAndSentimentClassification.pdf` | 29 |
| S5 | `5_LogisticRegression.pdf` | 15 |
| S6 | `6_VectorSemanticsAndEmbeddings.pdf` | 45 |
| S7 | `7_NeuralNetworksAndNeuralLanguageModels.pdf` | 17 |
| S8 | `8_RNNsAndLSTMs.pdf` | 64 |
| S9 | `9_theTransformer.pdf` | 34 |
| S10 | `10_LargeLanguageModels.pdf` | 26 |
| S11 | `11_MaskedLMs.pdf` | 47 |
| S12 | `12_Model AlignmentPromptingIn-ContextLearning_v2.0.pdf` | 46 |
| S13 | `13_MachineTranslation_v2.0.pdf` | 51 |
| S14 | `14_QuestionAnsweringAndIRAndRAG.pdf` | 24 |
| S15 | `15_ChatbotsAndDialogSystems.pdf` | 42 |
| S17 | `17_SequenceLabelingforPOSAndNER.pdf` | 33 |
| S18 | `18_ConstituencyGrammarsAndConstituencyParsing.pdf` | 63 |
| S19 | `19_DependencyParsing.pdf` | 34 |
| SL | `19B_LogicalRepresentationsOfSentenceMeaning.pdf` | 27 |
| S20 | `20_InformationExtractionRelationsEventsAndTime.pdf` | 43 |
| S21 | `21_SemanticRoleLabeling.pdf` | 31 |
| S22 | `22_LexiconsForSentimentAffectAndConnotation.pdf` | 34 |
| S23 | `23_CoreferenceResolution.pdf` | 51 |
| S24 | `24_DiscourseCoherence.pdf` | 25 |
| SH | `_A_HiddenMarkovModels.pdf` | 36 |

Historical corroboration in the same archive:

- [E1] `old exams _ gees/Mock Exam WS2122.pdf`, 14 pages.
- [E2] `old exams _ gees/Mock Exam Solution.pdf`, 35 pages.
- [E3] `old exams _ gees/GEE from July 1st, 2020.pdf`, 10 pages.
- [E4] `old exams _ gees/GEE from Feb 24, 2021.pdf`, 12 pages.
- [E5] `old exams _ gees/Fact sheet for the GEE on Feb 24, 2021.pdf`, 7 pages.
- [E6] `Course Information and Exam/OLD WS 23-24 Exam Fact Sheet.pdf`, 4 pages; historical organization only.

Academic metadata is established by the transcript and `01_inventory/courses.csv`, not inferred from these slides. Regenerable extraction/visual evidence: `.cache/in2361/evidence_manifest.json`, `.cache/in2361/text/`, `.cache/in2361/rendered/`.
