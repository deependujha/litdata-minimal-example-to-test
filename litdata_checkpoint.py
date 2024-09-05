import os
from litdata import optimize

def compress_failing(index):
    if index ==220:
        raise ValueError("220!!!!")
    return (index, index ** 2, "Hello world from litdata!")

def compress(index):
    return (index, index ** 2, "Hello world from litdata!")


data_store_uri = "s3://my-dummy-bucket-litdata/fsspec-testing"
data_store_uri = "gs://deependu-gcp-first-bucket/alpha"

if __name__ == '__main__':
    try:
        optimize(
            fn=compress,
            inputs=list(range(1000)),
            chunk_size=10,
            num_workers=2,
            output_dir=data_store_uri,
            use_checkpoint=True,
        )
    except ValueError:
       ...
       # optimize(
      #      fn=compress_failing,
     #       inputs=list(range(1000)),
    #        num_workers=2,
   #         chunk_size=10,
  #          output_dir=data_store_uri,
 #           use_checkpoint=True,
#        )

