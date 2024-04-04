#!/usr/bin/python
import boto3
import requests


def fetch_metadata(path):
    metadata_url = 'http://169.254.169.254/latest/meta-data/'
    token_url = 'http://169.254.169.254/latest/api/token'
    headers = {'X-aws-ec2-metadata-token-ttl-seconds': '60',
               'Content-Type': 'application/x-www-form-urlencoded'}

    # Retrieve IMDSv2 token

    token_response = requests.put(token_url, headers=headers)
    if token_response.status_code != 200:
        print('Failed to retrieve IMDSv2 token.')
        return None

    token = token_response.text
    headers_with_token = {'X-aws-ec2-metadata-token': token}
    url = metadata_url+path
    response = requests.get(url, headers=headers_with_token)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        return None


def get_instance_metadata():

    # Base URL for AWS instance metadata service

    metadata_url = 'http://169.254.169.254/latest/meta-data/'
    token_url = 'http://169.254.169.254/latest/api/token'
    headers = {'X-aws-ec2-metadata-token-ttl-seconds': '60',
               'Content-Type': 'application/x-www-form-urlencoded'}

    # Retrieve IMDSv2 token

    token_response = requests.put(token_url, headers=headers)
    if token_response.status_code != 200:
        print('Failed to retrieve IMDSv2 token.')
        return None
    token = token_response.text
    headers_with_token = {'X-aws-ec2-metadata-token': token}
    url=metadata_url
    response = requests.get(url, headers=headers_with_token)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        return None


if __name__ == '__main__':
    instance_metadata = get_instance_metadata()
    print(instance_metadata)
    instance_metadata = instance_metadata.split('\n')
    if instance_metadata:
        print('Fetched metadata keys and values:')

        while True:
            input_key = \
                input("\nEnter a key to fetch its value (or 'exit' to quit): ")
            if input_key.lower() == 'exit':
                break
            else:
                value = fetch_metadata(input_key)
                if value is not None:
                    print("Value for key '{}': {}".format(input_key, value))
                else:
                    print("Key '{}' not found in metadata.".format(input_key))
    else:
        print('Failed to retrieve instance metadata.')
