import argparse

import mlflow
import ray
from flaml import AutoML
from sklearn.datasets import load_diabetes
from tensorboardX import SummaryWriter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--redis-password", default='password')
    args = parser.parse_args()
    password = args.redis_password

    ray.init('auto', _redis_password=f'{password}')
    # Initialize an AutoML instance
    automl = AutoML()
    # Specify automl goal and constraint
    automl_settings = {
        "time_budget": 300,  # in seconds
        "metric": 'mse',
        "task": 'regression',
        "log_type": 'all',
        "n_concurrent_trials": 3,
        "log_file_name": "./outputs/diabetes.log",
        "log_training_metric": True,
        "log_type": 'all',
        "append_log": True,
    }
    
    X_train, y_train = load_diabetes(return_X_y=True)

    # Train with labeled input data
    # TODO: mlflow logging to Azure ML
    mlflow.log_param("n_concurrent_trials", automl_settings['n_concurrent_trials'])
    mlflow.log_param("task", automl_settings['task'])
    mlflow.log_param("metric", automl_settings['metric'])
    mlflow.log_param("time_budget", automl_settings['time_budget'])


    try:
        automl.fit(X_train=X_train, y_train=y_train, **automl_settings)
    except Exception as e:
        print(e)
    finally:
        print('Best ML leaner:', automl.best_estimator)
        print('Best hyperparmeter config:', automl.best_config)
        print('Best MSE: ', automl.best_loss)

        from flaml.data import get_output_from_log
        time_history, best_valid_loss_history, valid_loss_history, config_history, metric_history = \
            get_output_from_log(filename=automl_settings['log_file_name'], time_budget=240)
        print(time_history, best_valid_loss_history, valid_loss_history, config_history, metric_history)
        
        with SummaryWriter(comment='azureml', log_dir="logs/azureml/") as writer:
            for config, metric in zip(config_history, metric_history):
                hparam_dict_learner = {key: value for key, value in config.items() if key == 'Current Learner'}
                hparam_dict_param = config['Current Hyper-parameters']['ml']
                writer.add_hparams(hparam_dict=dict(**hparam_dict_learner, **hparam_dict_param), metric_dict=metric)
                mlflow.log_metric("mse", metric['train_loss'])

        import matplotlib.pyplot as plt
        import numpy as np

        fig = plt.figure()
        plt.title('Learning Curve')
        plt.xlabel('Wall Clock Time (s)')
        plt.ylabel('mse')
        plt.scatter(time_history, np.array(valid_loss_history))
        plt.step(time_history, np.array(best_valid_loss_history), where='post')
        plt.savefig("figure.png")
        mlflow.log_figure(fig, "figure.png")
        plt.show()

        ray.shutdown()
    
