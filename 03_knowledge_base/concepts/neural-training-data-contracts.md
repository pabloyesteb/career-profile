---
id: "neural-training-data-contracts"
title: "Neural approximation, training objectives and data contracts"
domains:
  - "machine-learning"
  - "optimization"
  - "scientific-software-data-engineering"
evidence_refs:
  - "mgt001299:neural-training"
  - "mgt001299:teaching-tools"
  - "ei7263:robot-learning-tools"
  - "ma4802:neural-architectures"
  - "ma4802:teaching-tools"
  - "additional-foml:network-optimization"
  - "tum-machine-learning-optimization:neural-tools"
  - "ma8102:loss-scaling"
  - "ma8102:typed-search"
  - "ma8102:reproducibility-tests"
  - "in2361:sequence-models"
  - "additional-cognitive-systems:statistical-examples"
  - "additional-cognitive-systems:feature-binding"
  - "scientific_paper:regression-preparation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "signed-distance-neural-fields"
---


# Neural approximation, training objectives and data contracts

## Approximation and optimization are different questions

Feature-linear and multilayer models address large state/data spaces. Feed-forward networks compose affine maps and sigmoid/tanh/ReLU-type activations; softmax/logistic outputs model class probabilities, while linear outputs support regression. The universal approximation theorem is a representation statement, not a training/generalization guarantee. CNNs/RNNs are introduced as alternatives without full assignment architectures.

Logistic regression uses linear log-odds; multiclass log-linear models normalize class-specific scores by a partition function. Maximum likelihood yields negative-log-likelihood minimization; MSE, binary log loss and categorical cross-entropy suit different targets. Deep RL exercises derive logistic gradients through multiplication/addition/negation/exponential/reciprocal nodes, construct XOR and show that identical-input squared-error predictions average inconsistent labels. A sheet's scalar sigmoid is not a softmax merely because its label says so.

Backpropagation applies the computational-graph chain rule. Batch/stochastic/minibatch gradients differ in sampling; constant/time/step/exponential/adaptive learning-rate schedules differ from convergence guarantees. SGD, Adam and RMSprop are supplied options. Epochs over a supervised dataset are not environment episodes.

## Framework and from-scratch examples

Deep RL provides TensorFlow/Keras subclassed, Sequential and functional models: wine regression (64/64 ReLU), Iris classification (10/10 ReLU), and bank classification (100/100/10 sigmoid). `tf.data`, feature stacking, `GradientTape`, explicit optimization/metrics and `compile`/`fit`/`evaluate` illustrate alternative workflows. Data handling uses pandas, one-hot/label conversion, missing-row handling and scikit-learn splits; wine standardization uses training-set means/standard deviations.

Humanoid tutorials provide NumPy affine layers, activation/output choices, random scaled initialization, biases, shuffled minibatch SGD and explicit `forward`/`backprop`/`update_batch`/`train`. MNIST precedes a marker-image-to-shoulder-angle regressor. Synchronized visual/joint data, normalization and output denormalization form the inference contract. Fixed head/elbow and ignored depth limit it to that setup, not general inverse kinematics.

## Data validity and software boundaries

Training/validation/test roles separate fitting, hyperparameter/stopping selection and evaluation. The supplied bank pipeline leaves both target columns: one becomes a model input, invalidating any inferred held-out accuracy. Humanoid submissions use z-scores despite requested [0,1] scaling and disagree on normalization/model paths; missing inference modules and placeholder/derivative-label errors limit turnkey reuse. Archive sample/model files and videos establish resources, not an independently measured personal result.

These contracts complement graph index alignment and learned-SDF derivative interfaces. Neither framework familiarity nor presence of submitted team code proves individual implementation of every network. Evidence: [Deep RL](../evidence/mgt001299.yaml) and [humanoid](../evidence/ei7263.yaml) teaching/tool claims. The specifically attributed SIREN contribution remains in its separate project claim rather than being generalized to all these resources.

## Architectural choices and optimization conditioning

Statistical Learning and supplementary ML add the distinction between shared-weight spatial filtering and dense layers. The usual deep-learning “convolution” computes cross-correlation; kernel/channel sizes, stride, padding and dilation determine the receptive field and output geometry. Standard versus depthwise filters allocate parameters differently: for a \(k\times k\) spatial kernel and \(C_{\rm in},C_{\rm out}\) channels, the filter-weight counts are \(k^2C_{\rm in}C_{\rm out}\) versus \(k^2C_{\rm in}\), excluding biases and any additional pointwise layer. Pooling, batch normalization, dropout and residual connections address different representation/training issues; saliency maps are an interpretation tool, not causal proof.

Depthwise **separable** convolution also includes a \(1\times1\) channel-mixing stage: its total filter count is \(k^2C_{\rm in}+C_{\rm in}C_{\rm out}\). Xception/MobileNet illustrate this distinction from depthwise filtering alone. Batch normalization normalizes minibatch activations with a stabilizing epsilon and learns scale/shift. Leaky ReLU addresses inactive negative-side units; repeated test-time dropout is a represented uncertainty heuristic, not a calibrated-coverage result.

The corpus includes LeNet/AlexNet/ResNet and U-Net vision/reconstruction/segmentation contexts. Neural interpretation includes filter visualization, occlusion, input class-score maximization, gradient saliency, class activation maps and PCA/t-SNE feature visualization; a full t-SNE algorithm is not supplied. Multitask heads share internal representations, multimodal models combine modality-specific inputs, and transfer learning reuses pretrained features when labels are scarce. Microscopy, genomics and medical imaging motivate these distinctions.

Introductory Transformer coverage distinguishes token/positional embeddings, multi-head self-attention, masked decoder attention, cross-sequence attention, feed-forward blocks and residual/normalization paths. ViT embeds image patches plus class/position tokens; HistoGPT connects a histology encoder through a resampler/cross-attention to a biomedical language model, separating frozen pretrained components from trained connectors. These architecture diagrams do not supply a scaled-dot-product derivation or establish personally trained foundation models. Supplementary GPT material adds the tokenization → Transformer → next-token probabilities → cross-entropy pipeline; implementation of that pipeline is not personally attributed.

FOML connects activations, initialization, normalization, residual paths, adaptive gradients and regularization to [optimization](first-order-stochastic-optimization.md), without turning heuristic training advice into a global convergence theorem. Teaching tools include Python, NumPy/SciPy, pandas, scikit-learn, Matplotlib/Seaborn, Jupyter/Colab and supplementary PyTorch/torchvision/tqdm. MA4802 names PyTorch tutorials and illustrative Keras examples, not personally authored trained systems. Clinical/classification and house-price/MNIST examples remain teaching resources. Source-specific evidence is in [MA4802](../evidence/ma4802.yaml) and [supplementary ML](../evidence/tum-machine-learning-optimization.yaml).

## Implemented regression losses, metric spaces and numerical guards

pyLowOrder adds attributable code rather than another educational example. For residual \(e=\hat y-y\), its focal regression objective is
\[
L_{\rm focal}=\operatorname{mean}\big[(|e|+\epsilon)^\gamma e^2\big],
\]
with mean/sum reduction; the target-weighted alternative is \(\operatorname{mean}[(1+\alpha|y|)e^2]\). The first emphasizes residual magnitude; the second weights by target magnitude. Neither is focal classification loss or an empirically established improvement.

Training loss, validation checkpoint metric and Optuna objective must be distinguished. Checkpoints can select loss or MAE; an explicitly supplied inverse output transformation enables physical/output-space MAE. Epoch metrics average batch metrics, not necessarily a globally sample-weighted estimate. Best-state restoration includes model/optimizer/scheduler. The Optuna objective nevertheless uses final logged validation loss, so it is not automatically the restored checkpoint's score.

Finite checks cover predictions, targets, loss and gradients. Optional norm clipping precedes updates, while epoch-zero loss and JSONL diagnostics support numerical inspection. Authored exact-state/forward/loss-sequence tests document validation procedures, not verified passing executions or convergence.

## Scaling is an inference contract

The implemented scalers include grouped-vector MinMax and standard/robust transforms:
\[
x_{\rm mm}=a+\frac{x-x_{\min}}{x_{\max}-x_{\min}}(b-a),\qquad
x_{\rm std}=\frac{x-\mu}{\sigma},\qquad
x_{\rm robust}=\frac{x-\operatorname{median}(x)}{Q_{75}-Q_{25}}.
\]
For standard/robust fitting a list supplies separate variable blocks; one matrix is one block, not automatically featurewise fitting. Near-zero standard deviation/IQR uses one. NumPy/Torch inverse transforms and serialized parameters restore output units; robust percentiles are fitted on CPU. This matters when geometry, vector components and pressure targets cross data/model boundaries. It does not establish an empirical gain from a particular normalization.

[pyLowOrder claims](../evidence/ma8102.yaml), loss-scaling, typed-search and reproducibility-tests, preserve commit locators and the distinction between implemented safeguards and measured outcomes.

## Sequence, feature and multi-output contracts

NLP now supplies detailed recurrence/BPTT, gated memory, QKV attention, causal/positional context and low-rank adaptation in the canonical [sequence-language page](neural-sequence-language-models.md). An encoder's available context, token-label alignment and KV cache differ from independent tabular/mesh samples. These details are not duplicated here.

Cognitive Systems adds explicit Sobel/Gabor filters, SIFT/Fourier/DTMF feature examples, the convolution theorem as an acceleration idea, Neocognitron/Inception milestones and capsule/EM-routing binding hypotheses. Transform overhead and the absence of an FFT-CNN implementation matter. Its `PolynomialFeatures + Ridge`, perceptron and vectorized NumPy exercises are supplied teaching code, not new personally completed projects.

NGValidation uses multi-output loss displays with component aggregation left implicit and an unsquared printed L2 norm; neither is silently replaced with an invented target weighting or squared penalty. Geometry-aware preprocessing/PCA is fitted on training data only. The paper gives general MLP/CNN/recurrent/reservoir/GNN alternatives and optimizer choices, not an exact industrial network/training specification.
