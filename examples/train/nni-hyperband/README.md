# HyperParameter Tuning HyperBand with NNI

This example shows how to use NNI to perform hyperparameter tuning with HyperBand on Azure Machine Learning.

## Prerequisites

- Azure Machine Learning Workspace
    - Compute Clusters for parallel training
    - Compute Instance with Azure ML CLI 2.0 and NNI library installed

## Getting Started

1. Install NNI library in your Compute Instance.

```bash
pip install nni
```

2. Create a train script and a configuration file.

3. Start trial job.

```bash
nnictl create --config config_hyperband.yml --port 8888
```

4. Access to dashboard.


## HPO with NNI

Neural Network Intelligence (NNI) is a library that provides a unified interface for hyperparameter optimization. Many tuning algorithm is included. See the following link for more details in reference section.

## Reference

- [Neural Network Intelligence (NNI)](https://github.com/microsoft/nni)

