import os
import requests
import csv

def main():
    # Create arg parser
    parser = argparse.ArgumentParser(description='Script to fetch glossary terms by glossary ID.')

    # Add arguments
    parser.add_argument(
        '--token',
        type=str,
        default=os.environ.get('ALATION_TOKEN', None),
        required=os.environ.get('ALATION_TOKEN', None) is None,
        help='Alation API Token'
    )

    parser.add_argument(
        '--base_url',
        type=str,
        default=os.environ.get('BASE_URL', None),
        required=os.environ.get('BASE_URL', None) is None,
        help='Base URL for your Alation instance (i.e., "alation.mydomain.com")'
    )

    parser.add_argument(
        '--glossary_id',
        type=str,
        default=os.environ.get('GLOSSARY_ID', None),
        required=os.environ.get('GLOSSARY_ID', None) is None,
        help='Alation Glossary ID'
    )

    api_token = args.token
    base_url = args.base_url
    glossary_id = args.glossary_id

    # Define the API endpoint and headers
    url = f'https://{base_url}/integration/v2/term/?glossary_id={glossary_id}&limit=100&skip=0&deleted=false'
    headers = {
        'TOKEN': api_token,
        'accept': 'application/json'
    }

    # Send GET request to the API
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Create output directory if it doesn't exist
        output_dir = './output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define CSV file path
        csv_filename = os.path.join(output_dir, 'alation_data.csv')

        # Write data to CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        print(f'Data has been successfully written to {csv_filename}')
    else:
        print(f'Error: {response.status_code}')


if __name__ == "__main__":
    main()