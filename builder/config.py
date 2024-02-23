import os


dirname = os.path.dirname(__file__)

config = {
    'gov_source_url': 'https://raw.githubusercontent.com/cisagov/dotgov-data/main/current-federal.csv',
    'pulse_source_url': 'https://raw.githubusercontent.com/GSA/data/master/dotgov-websites/pulse-subdomains-snapshot-06-08-2020-https.csv',
    'dap_source_url': 'https://analytics.usa.gov/data/live/sites-extended.csv',
    'omb_source_url': 'https://resources.data.gov/schemas/dcat-us/v1.1/omb_bureau_codes.csv',
    'omb_idea_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/omb_idea.csv',
    '2020_eotw_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/2020_eot.csv',
    'usagov_directory_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/usagov_directory.csv',
    'gov_man_22_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/gov_man-22.csv',
    'usacourts_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/uscourts.csv',
    'oira_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/oira.csv',
    'mil_source_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/dotmil_websites.csv',
    'mil_source_url_2': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/dotmil_websites-2.csv',
    'mil_domains_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/dataset/dotmil_domains.csv',
    'other_websites_path': os.path.join(dirname, '../data/dataset/other-websites.csv'),
    'ignore_list_begins_path': os.path.join(dirname, '../criteria/ignore-list-begins.csv'),
    'ignore_list_contains_path': os.path.join(dirname, '../criteria/ignore-list-contains.csv'),
    'target_url_list_path': os.path.join(dirname, '../data/site-scanning-target-url-list.csv'),
    'gov_snapshot_path': os.path.join(dirname, '../data/snapshots/gov.csv'),
    'pulse_snapshot_path': os.path.join(dirname, '../data/snapshots/pulse.csv'),
    'dap_snapshot_path': os.path.join(dirname, '../data/snapshots/dap.csv'),
    'omb_idea_snapshot_path': os.path.join(dirname, '../data/snapshots/omb_idea.csv'),
    '2020_eotw_snapshot_path': os.path.join(dirname, '../data/snapshots/2020_eot.csv'),
    'usagov_directory_snapshot_path': os.path.join(dirname, '../data/snapshots/usagov_directory.csv'),
    'gov_man_22_snapshot_path': os.path.join(dirname, '../data/snapshots/gov_man_22.csv'),
    'usacourts_snapshot_path': os.path.join(dirname, '../data/snapshots/usacourts.csv'),
    'oira_snapshot_path': os.path.join(dirname, '../data/snapshots/oira.csv'),
    'other_snapshot_path': os.path.join(dirname, '../data/snapshots/other.csv'),
    'combined_snapshot_path': os.path.join(dirname, '../data/snapshots/combined.csv'),
    'remove_ignore_begins_path': os.path.join(dirname, '../data/snapshots/remove-ignore-begins.csv'),
    'remove_ignore_contains_path': os.path.join(dirname, '../data/snapshots/remove-ignore-contains.csv'),
    'deduped_snapshot_path': os.path.join(dirname, '../data/snapshots/combined-dedup.csv'),
    'dedup_removed': os.path.join(dirname, '../data/snapshots/dedup-removed.csv'),
    'ignored_removed_begins': os.path.join(dirname, '../data/snapshots/ignored-removed-begins.csv'),
    'ignored_removed_contains': os.path.join(dirname, '../data/snapshots/ignored-removed-contains.csv'),
    'nonfederal_removed': os.path.join(dirname, '../data/snapshots/nonfederal-removed.csv'),
    'analysis_csv_path': os.path.join(dirname, '../data/site-scanning-target-url-list-analysis.csv'),
    'url_df_pre_base_domains_merged': os.path.join(dirname, '../data/test/url_df_pre_base_domains_merged.csv'),
    'url_df_post_base_domains_merged': os.path.join(dirname, '../data/test/url_df_post_base_domains_merged.csv'),
}