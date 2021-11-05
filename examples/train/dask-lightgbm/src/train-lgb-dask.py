import argparse
import pickle
from re import VERBOSE
import time

import dask.dataframe as dd
import joblib
import lightgbm as lgb
import mlflow
from dask.distributed import Client, LocalCluster, performance_report, wait

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path")
    args = parser.parse_args()
    dataset_path = args.dataset_path

    OUTOUT_DIR = './outputs'

    print("loading data")
    df = dd.read_csv(f"{dataset_path}/*.csv", parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"])

    df["total"] = df["total_amount"] + df["tolls_amount"] + df["tip_amount"] + df["extra"]

    dX = df.drop(["store_and_fwd_flag", "tpep_pickup_datetime", "tpep_dropoff_datetime", "total", "total_amount", "tolls_amount", "tip_amount", "extra"], axis=1)
    dy = df["total"]

    print("initializing a Dask cluster")

    #cluster = LocalCluster(dashboard_address=':9999') # port 8787 is already used by R studio server
    #client = Client(cluster)

    client = Client("localhost:8786")

    print("created a Dask LocalCluster")

    dX.persist()
    dy.persist()
    wait(dX)
    wait(dy)
    print("distributing training data on the Dask cluster")

    print("beginning training")
    dask_model = lgb.DaskLGBMRegressor(n_estimators=100)

    with performance_report(filename="./outputs/dask-report.html"):
        start = time.time()
        dask_model.fit(dX, dy, verbose=5)
        elapsed_time = time.time() - start
        print("elapsed time: {}".format(elapsed_time))
        mlflow.log_metric("training_time", elapsed_time)
        assert dask_model.fitted_
        
    # Save sklearn Estimator Model
    sklearn_model = dask_model.to_local()
    joblib.dump(sklearn_model, "./outputs/dask-sklearn-model.joblib")

    # Save Dask LightGBM Model
    with open("./outputs/dask-model.pkl", "wb") as f:
        pickle.dump(dask_model, f)

    print("done training")




