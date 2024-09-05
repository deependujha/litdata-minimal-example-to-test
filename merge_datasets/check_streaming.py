import litdata as ld

#s3_uri = 's3://my-dummy-bucket-litdata/fsspec-testing'
#s3_uri = 'gs://deependu-gcp-first-bucket/alpha'

s3_uri = 'abfs://blob-container/my-optimized-dataset-merge/data3'
s3_uri = 'abfs://blob-container/my-optimized-dataset-merge/final_data'

storage_options= {"account_name":"litdatafsspec", "account_key":""}


dataset = ld.StreamingDataset(s3_uri, shuffle=True, storage_options=storage_options)
dataloader = ld.StreamingDataLoader(dataset)

print(f"{len(dataloader)=}")

for sample in dataloader:
    print(sample)
    print("="*80)
print("\nAll done\n")
