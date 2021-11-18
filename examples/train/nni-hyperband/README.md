# HyperParameter Tuning HyperBand with NNI

This example shows how to use NNI to perform hyperparameter tuning with HyperBand on Azure Machine Learning.


## HPO with NNI

Neural Network Intelligence (NNI) is a library that provides a unified interface for hyperparameter optimization. Many tuning algorithm is included. See the following link for more details in reference section.


## Prerequisites

- Azure Machine Learning Workspace
    - Compute Clusters for parallel training
    - Compute Instance with Azure ML CLI 2.0 and NNI library installed

## Getting Started

1. Create conda environment

  ```bash
  conda create -n nni python=3.6
  conda init bash
  source ~/.bashrc
  conda activate nni
  ```

2. Install NNI library in your Compute Instance.

  ```bash
  pip install nni==2.5 azureml-sdk==1.35.0
  ```
3. Create Compute Clusters in your Azure Machine Learning Workspace

<!-- TODO: Azure CLI and YML to create Compute Clusters -->

4. Create a train script, a job configuration file and a search space configuration file.
 
- train script : train.py

<!-- TODO: explain the points of the codes-->

- job configuration file : config_hyperband.yml

  configure TrainingService to Azure Machine Learning.

  ```yml
  TrainingService:
    platform: aml
    dockerImage: msranni/nni  # modify this if you bring your own docker image
    subscriptionId: <your subscription ID>
    resourceGroup: <azure machine learning workspace resource group>
    workspaceName: <azure machine learning workspace name>
    computeTarget: <compute cluster name>
  ```

- search space configuration file : search_space.json

  define your search space of hyperparameters in json file.

  ```json
  {
      "dropout_rate":{"_type":"uniform","_value":[0.5,0.9]},
      "conv_size":{"_type":"choice","_value":[2,3,5,7]},
      "hidden_size":{"_type":"choice","_value":[124, 512, 1024]},
      "batch_size": {"_type":"choice","_value":[8, 16, 32, 64]},
      "learning_rate":{"_type":"choice","_value":[0.0001, 0.001, 0.01, 0.1]}
  }
  ```

5. Start trial job.

  ```bash
  nnictl create --config config_hyperband.yml --port 8088
  ```

6. Access to dashboard.
  - NNI Dashboard is running on Compute Instance. You can access to it from your client PC from URL like `https://<your compute instance name>-8088.<region>instances.azureml.ms` and check the result as blew. For examples, if your Compute Instance name is "client" and region is "japaneast", you can access using `https://client-8088.japaneast.instances.azureml.ms`. <img src="../../../docs/images/nni-1.png"><img src="../../../docs/images/nni-2.png"><img src="../../../docs/images/nni-3.png"><img src="../../../docs/images/nni-4.png"><img src="../../../docs/images/nni-5.png">




## Reference

- [Neural Network Intelligence (NNI)](https://github.com/microsoft/nni)

