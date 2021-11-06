import threading
import sys
import subprocess
import os
import argparse
from mpi4py import MPI

def flush(proc, proc_log):
    while True:
        proc_out = proc.stdout.readline()
        if proc_out == "" and proc.poll() is not None:
            proc_log.close()
            break
        elif proc_out:
            sys.stdout.write(proc_out)
            proc_log.write(proc_out)
            proc_log.flush()

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    mpi_rank = comm.Get_rank()
    print("mpi rank:", mpi_rank)

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default="6379", type=int)
    parser.add_argument("--script", type=str)
    args = parser.parse_args()

    # this scirpt is for flaml automl training
    script = args.script

    # port for ray head node
    port = args.port
    print("head port is ", port)

    head_ip = os.environ.get("MASTER_ADDR")
    print("head address is ", head_ip)

    rank = os.environ.get("RANK")
    print("my rank is ", rank)

    # TODO:Get Password from Azure KeyVault
    password = "password"

    # Ray Head Node
    if str(rank) == "0":
        head_log = open("logs/worker_{rank}_log.txt".format(rank=rank), "w")

        cmd = f"ray start --head --port={port} --redis-password={password} --dashboard-port=9999"
        print(cmd)
        
        head_proc = subprocess.Popen(
            cmd.split(),
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        head_flush = threading.Thread(
            target=flush, args=(head_proc, head_log)
        )
        head_flush.start()

        python_log = open("logs/python_{rank}_log.txt".format(rank=rank), "w")
        command_line = f"python {script} --redis-password={password}"
        driver_proc = subprocess.Popen(
            command_line.split(),
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        driver_flush = threading.Thread(
            target=flush, args=(driver_proc, python_log)
        )
        driver_flush.start()
        driver_proc.wait()  

        head_proc.kill()
        driver_proc.kill()
        print("### Head Job Finished")


    # Ray Worker Node
    else:
        worker_log = open("logs/worker_{rank}_log.txt".format(rank=rank), "w")
        cmd = f"ray start --address={head_ip}:{port} --redis-password {password}"
        print(cmd)
        worker_proc = subprocess.Popen(
            cmd.split(),
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        flush(worker_proc, worker_log)
        # worker_flush = threading.Thread(
        #     target=flush, args=(worker_proc, worker_log)
        # )
        # worker_flush.start()
        # worker_proc.wait()

