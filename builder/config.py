from datetime import datetime
import os


dirname = os.path.dirname(__file__)

config = {
    'gov_source_url': 'https://raw.githubusercontent.com/cisagov/dotgov-data/main/current-federal.csv',
    'pulse_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/snapshots/1-13-22/pulse-subdomains-snapshot-06-08-2020-https.csv',
    'dap_source_url': 'https://analytics.usa.gov/data/live/sites-extended.csv',
    'todays_snapshot_path': os.path.join(dirname, '../data/snapshots/' + datetime.now().strftime('%Y-%m-%d')),
    'additional_data_path': os.path.join(dirname, '../data/dataset/other-websites.csv'),
    'ignore_list_path': os.path.join(dirname, '../criteria/ignore-list.csv'),
    'omb_source_url': 'https://resources.data.gov/schemas/dcat-us/v1.1/omb_bureau_codes.csv',
    'target_url_list_path': os.path.join(dirname, '../data/temp/site-scanning-target-url-list.csv')
}