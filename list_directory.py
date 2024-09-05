from litdata.streaming.downloader import list_directory

azure_uri = 'azure://blob-container/my-dataset'
azure_uri = 'abfs://blob-container/my-dataset'

meow = list_directory(azure_uri,storage_options= {"account_name":"litdatafsspec", "account_key":""})


print(f"{meow=}")
