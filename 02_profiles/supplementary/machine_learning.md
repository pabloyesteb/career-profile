# Machine Learning and Optimization — supplementary academic materials

## Identity and provenance

| Field | Value |
|---|---|
| Stable source ID | tum-machine-learning-optimization |
| Source identity | EI71058: Machine Learning and Optimization; Prof. Reinhard Heckel, TUM |
| Archive term | Winter Semester 2025/26 |
| source_category | supplementary_academic_material |
| academic_credit | not_established |
| learning_relationship | unspecified |
| Profile status | complete_validated |

The introduction explicitly supplies EI71058, supplementing the older index inventory that had no code. It is **not a transcript code or new academic record**, and the user's earlier decision that this is not Fundamentals of Optimization for Machine Learning is preserved. The user authorizes supplementary inclusion; the exact learning relationship remains unspecified. Neither completed assignments nor personal implementations/mastery are inferred. Inspected 2026-10-15.

## Available materials and extraction approach

Archive: `00_sources/tum/archives/Machine Learnin 950839125 (W25_26)_20261012_1602.zip`. Its 96 files include 55 PDFs, four `.ipynb` files, 13 JSON files (some contain notebook cells), a CSV, three `.imscc` packages and administrative pages. Weekly organization supplies 12 lecture-note/slide documents, homework/solutions, tutorials, coding examples, an introduction and historical exams. All lecture documents' heading/topic structure was inspected, with selected detailed text, notebook imports, and visual review of the training-data deck's GPT training diagram (p. 12). No notebook/code was executed; nested dataset packages were not fully unpacked.

## Technical topic map

### Regression, regularization and evaluation

Linear least squares is developed through convex-optimization and linear-algebra arguments, including collinearity, ridge estimates and bias–variance trade-offs. Model selection distinguishes training, validation and test risks. Logistic and multiclass logistic regression connect probabilistic classification to gradient-based fitting. [N1–2, N4.]

Statistical learning theory includes no-free-lunch discussion, generative/discriminative distinctions, empirical versus population risk, uniform convergence, Hoeffding bounds/union bounds and algorithmic stability. The archive therefore links optimization error and generalization rather than only listing supervised predictors. Early stopping for least squares introduces **algorithmic regularization**. [N5–6.]

### Optimization algorithms

Convexity, quadratic gradient-descent convergence and stochastic-gradient analysis accompany incremental gradients, soft-margin classification, population-risk minimization, stochastic approximation and coordinate descent. Epoch/momentum concepts precede acceleration and adaptive updates: **Nesterov acceleration, AdaGrad and Adam**. The adaptive-method note gives an illustrative diagonal least-squares AdaGrad convergence analysis, not an unrestricted rate for every ML objective. Randomized Kaczmarz is explicitly marked additional reading not discussed in class; it belongs to the supplied corpus with that distinction. [N3, N10.]

### Margins, kernels and nonlinear predictors

Perceptron, hard/soft-margin SVM, Lagrangian duality, dual SVM formulation, nonlinear features, the **representer theorem** and Gaussian kernels build a kernel-method block. This supplies both optimization and function-representation viewpoints. [N7, §§11–12.]

### Neural networks and vision

Neural architectures, optimization, automatic differentiation and vanishing gradients lead into convolutional networks. Local connectivity and shift equivariance motivate convolutional inductive bias; channels, learned kernels, stride, padding and pooling control representation size and computation. Examples include LeNet, AlexNet, ResNet and U-net, with image classification, segmentation and reconstruction applications. [N8–9; CNN deck pp. 4–22.]

### Training data and language-model context

The final deck emphasizes leakage from feature selection/evaluation, distribution shift, pretraining versus task-specific fine-tuning, web-data quality and dataset evaluation at controlled model/compute/token scales. A GPT diagram explicitly shows tokenization → transformer → next-token probabilities with cross-entropy loss. The data-curation sequence includes heuristic filtering, deduplication and ML-based quality filtering, illustrated by DCLM/FineWeb/C4 examples; it is source-era context, not a current ranking of models or datasets. [N11, pp. 2–23, especially pp. 12–21.]

## Computational material, tools and applications

Static notebook/JSON cell inspection evidences **Python, NumPy, SciPy, pandas, scikit-learn, PyTorch, torchvision, Matplotlib and tqdm**. Named files include logistic-regression early stopping, MNIST, PyTorch neural-network exercises, a house-price CSV, `PyTorchFromScratch.json` and a GPT notebook JSON. Hitters/nuclear datasets are supplied as nested `.imscc` packages. Notebook presence is evidence of available exercises, not user authorship or successful training. The introduction names fraud detection, recommendations, NLP, self-driving and scientific signal reconstruction as applications, while actual represented examples include regression and image learning.

## Relationships and potential professional relevance

This material overlaps usefully with [Statistical Learning](../courses/ma4802-statistical-learning.md), [Foundations of Data Analysis](../courses/ma4800-foundations-of-data-analysis.md), [FOML](../courses/additional-foml-fundamentals-of-optimization-for-machine-learning.md), [NLP](../courses/in2361-natural-language-processing.md) and [Deep Generative Models](../courses/cit4230003-advanced-machine-learning-deep-generative-models.md), but is not a newly credited version of them. Generalization/data reliability connect to the [scientific paper](../projects/ngvalidation.md); optimizer/regularization/data workflows connect to [pyLowOrder](../projects/pyloworder.md) without changing that project's contribution evidence.

Potential domains: ML/data engineering, robust evaluation, scientific ML and quantitative predictive modeling. Thematic categories: machine learning; optimization; statistics and data science; software/data engineering.

## Source index and deeper-extraction priorities

All references resolve inside the named archive:

- Identity: `14. Oktober - 20. Oktober/Introduction Slides.pdf`, p. 1.
- **N1:** `14. Oktober - 20. Oktober/Lecture Notes Week 1 and 2 (Linear Regression, Ridge Regression).pdf` (10 pp.). **N2:** `21. Oktober - 27. Oktober/Lecture Notes 2 (model selection).pdf` (5 pp.).
- **N3:** `28. Oktober - 3. November/Lecture Notes Week 3(convex opt___nd stochastic gradient method).pdf` (13 pp.). **N4:** `4. November - 10. November/Lecture Notes Week 4(Logistic regression).pdf` (5 pp.).
- **N5:** `11. November - 17. November/Lecture Notes Week 5(Statistical learning theory).pdf` (9 pp.). **N6:** `18. November - 24. November/Lecture Notes Week 6(Algorithmic Regularization).pdf` (4 pp.).
- **N7:** `25. November - 1. Dezember/Lecture Notes Week 7 (SVM and Kernels).pdf` (14 pp.). **N8:** `9. Dezember - 15. Dezember/Lecture Notes 8(Neural Network).pdf` (7 pp.).
- **N9:** `16. Dezember - 22. Dezember/Lecture Notes Week 9 - CNN.pdf` (22 pp.). **N10:** `27. Januar - 2. Februar/Lecture Notes(Acceleration and adaptive gradient methods).pdf` (5 pp.). **N11:** `3. Februar - 9. Februar/Lecture Notes(Role of Training Data).pdf` (23 pp.).
- Computational anchors: `25. November - 1. Dezember/logistic_regression_with_early_stopping.ipynb`; `9. Dezember - 15. Dezember/mnist_homework.ipynb`; `16. Dezember - 22. Dezember/neural_networks_pytorch.ipynb`; `20. Januar - 26. Januar/Jupyter Notebook on GPT.json`.
- Inventory: stable source ID in `files_manifest.csv`; exact members in `archive_files.csv`.

The 11 numbered N references cover the available subject-note sequence; the introduction is separate, and N1 combines linear and ridge regression. Prioritize stability/generalization assumptions, early-stopping spectral analysis, kernel/representer derivations and optimizer rates; then inspect selected notebook objectives/data splits and dataset packages. Additional visual inspection should precede extracting detailed architecture/layout-dependent claims. This map covers the full available lecture-topic sequence without validating all homework, historical exams or every notebook result.
