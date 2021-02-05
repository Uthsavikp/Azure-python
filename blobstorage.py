''' 
  @Author: Uthsavi KP
  @Date: 2021-02-03 11:23:36
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-02-03 9:46:38
  @Title: Azure cosmosDB using python
'''

import os, uuid, sys
#from typing import Container
from azure.storage.blob import BlobServiceClient


def run_sample():
    try:
        block_blob_service = BlobServiceClient(account_name='123blobstorage', account_key='')

        container_name ='quickstartblobs'
        block_blob_service.create_container(container_name)

        
        local_path=os.path.abspath(os.path.curdir)
        local_file_name = input("Enter file name to upload : ")
        full_path_to_file = os.path.join(local_path, local_file_name)

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)

        block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)


        full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name , '.txt', '_DOMNLOADED.txt'))
        print("\nDownloading blob to " + full_path_to_file2)
        block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

        sys.stdout.write("Sample finished running. when you hit <any key>, the sample will be deleted and the sample "
                            "application will exit.")
        sys.stdout.flush()
        input()


        block_blob_service.delete_container(container_name)
        os.remove(full_path_to_file)
        os.remove(full_path_to_file2)
    except Exception as e:
        print(e)

if __name__=='__main__':
   run_sample()