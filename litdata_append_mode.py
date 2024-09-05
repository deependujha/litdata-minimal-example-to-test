import os
from litdata import optimize

def compress(index):
    return (index, index ** 2)

#data_store_uri = "s3://my-dummy-bucket-litdata/fsspec-testing"
#data_store_uri = "gs://deependu-gcp-first-bucket/alpha"

data_store_uri = 'abfs://blob-container/my-optimized-dataset'

storage_options= {"account_name":"litdatafsspec", "account_key":""}


if __name__ == '__main__':
    optimize(
        fn=compress,
        inputs=list(range(100,200)),
        num_workers=2,
        output_dir=data_store_uri,
        chunk_bytes="64MB",
        mode="append",
        storage_options = storage_options,
    )

