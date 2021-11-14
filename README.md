# Machine Learning at Scale on Azure Machine Learning

This repo is a collection of codes/notebooks for machine learning at scale on Azure Machine Learning. 

## Contents

### Train

|Folder/Files |Description|
|---------|-----------|
|[pytorch-dpp](examples/train/pytorch-ddp)| PyTorch Distributed Data Parallel (DDP) |
|[dask-lightgbm](examples/train/dask-lightgbm)| LightGBM Distributed Training with DASK |
|[ray-flaml](examples/train/ray-flaml)|FLAML AutoML with RAY|
|[nni-hyperband](examples/train/nni-hyperband)| HyperParameter Tuning HyperBand with NNI |

### Inference

Your contribution is welcome !

## Getting Started

### setup base environment*

1. Setup Azure Machine Learning Workspace in your Azure subscription. See [Manage Azure Machine Learning workspaces in the portal or with the Python SDK](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python) for more details.
2. Download and install Visual Studio Code in your client PC. And install Azure Machine Learning Extension. See [Azure Machine Learning in VS Code](https://code.visualstudio.com/docs/datascience/azure-machine-learning) for more details.
3. Create new Azure ML Compute Instance and launch Visual Studio Code. See [Connect to an Azure Machine Learning compute instance in Visual Studio Code (preview) - Configure a remote compute instance](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-set-up-vs-code-remote?tabs=studio#configure-a-remote-compute-instance) for more details.
4. Install Azure Machine Learning Cli 2.0. See [installation document](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli) for more details.

*These steps are not mandatory. There are the other ways to setup environment. But this repo is assumed to follow the above steps.



## Events
[2021-11-18] [DB TECH SHOWCASE 2021 (Japan)](https://www.db-tech-showcase.com/2021/schedule/) - D14 Microsoft : Azure Machine Learning で始める大規模機械学習 @ 女部田啓太


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
