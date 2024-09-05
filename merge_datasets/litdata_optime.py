import os, time
from litdata import optimize

def compress(index):
    return (index, index ** 2)

data_store_uri = "s3://my-dummy-bucket-litdata/fsspec-testing"
#data_store_uri = "gs://deependu-gcp-first-bucket/check_merge/"
data_store_uri = 'abfs://blob-container/my-optimized-dataset-merge/data'

storage_options= {"account_name":"litdatafsspec", "account_key":""}


if __name__ == '__main__':
    for i in range(5):
        optimize(
            fn=compress,
            inputs=list(range(100*i, 100*(i+1))),
            num_workers=2,
            output_dir=data_store_uri+str(i),
            chunk_bytes="64MB",
            storage_options=storage_options,
        )
        time.sleep(30)

