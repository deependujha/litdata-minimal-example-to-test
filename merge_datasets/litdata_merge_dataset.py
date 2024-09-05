from litdata import merge_datasets

data_store_uri = "s3://my-dummy-bucket-litdata/fsspec-testing"
#data_store_uri = "gs://deependu-gcp-first-bucket/check_merge/"
data_store_uri = 'abfs://blob-container/my-optimized-dataset-merge/data'
output_dirs = 'abfs://blob-container/my-optimized-dataset-merge/final_data'

storage_options= {"account_name":"litdatafsspec", "account_key":""}



if __name__=='__main__':
    input_dirs = [data_store_uri +str(i) for i in range(5)]
    print(f"{input_dirs=}")

    merge_datasets(input_dirs, output_dirs, storage_options=storage_options)
