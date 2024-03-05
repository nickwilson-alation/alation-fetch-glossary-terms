# Alation Fetch Glossary Terms

This script retrieves glossary terms from the Alation API and converts them to CSV format.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
3. Run the script `alation_to_csv.py` with the following arguments:

    - `--token`: Your Alation API Token. You can either provide it as an argument or set it as an environment variable named `ALATION_TOKEN`.

    - `--base_url`: The base URL for your Alation instance (i.e., "alation.mydomain.com"). Provide it as an argument or set it as an environment variable named `BASE_URL`.

    - `--glossary_id`: The Alation Glossary ID. You can provide it as an argument or set it as an environment variable named `GLOSSARY_ID`.

    ### Example:

    ```bash
    python main.py --token abc123abc123 --base_url alation.mydomain.com --glossary_id 1
    ```

4. The CSV file will be saved in the `output` folder.
