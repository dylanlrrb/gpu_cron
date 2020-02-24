# gpu_cron

A repo to version control the cron jobs requiring GPU that run on my desktop

It will periodically pull down the repos specified in `active_reops.txt` and poll for certain tags.

Tags that are not present in S3 are checked out and the jupyter notebooks there are executed in a docker container

The trained model  and html converted notebook from the execution are then upladed to S3 for later use

## Requirements

First, you will need to set up a virtual environment named `gpu_cron` with a python version >= 3.6 and `boto3`

Make sure you have AWS credentials set up to read from and write to the S3 bucket you want to store

## Cron setup

Example setup that runs every 15 minutes

```console
*****
```
