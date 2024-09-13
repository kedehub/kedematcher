# based on https://github.com/pyinstaller/pyinstaller/issues/2322
import multiprocessing as mp
if __name__ == '__main__':
    mp.freeze_support()
    mp.set_start_method('spawn')

import argparse
import sys
import time
from tqdm import tqdm
from kedehub.services.identities_updater import identity_merge_users, identity_merge_users_with_human_help
from kedehub.services.project_service import load_all_project_names

def identity_merge_project(options):
    verbose = options.verbose

    projects_to_update = options.project
    if not projects_to_update:
        projects_to_update = load_all_project_names()

    number_or_projects_to_update = len(projects_to_update)

    print("First pass...")
    len_users, lean_authors, len_matched_users_by_email, len_matched_users_by_email_and_name, \
    authors_updated, users_inserted, users_merged_count, authors_merged_count = identity_merge_users(projects_to_update, verbose)

    time.sleep(1)
    tqdm.write('Successfully merged {} into {} users with {} authors for {} projects. Created {} new users. '.format(len_users, len_matched_users_by_email_and_name, authors_updated, number_or_projects_to_update, users_inserted))

    print("Second pass...")
    len_users, lean_authors, len_matched_users_by_email, len_matched_users_by_email_and_name, \
    authors_updated, users_inserted, users_merged_count, authors_merged_count = identity_merge_users_with_human_help(projects_to_update, verbose)

    time.sleep(1)
    tqdm.write(
        'Successfully merged {} into {} users with {} authors for {} projects. Created {} new users. '.format(len_users,
                                                                                                              len_matched_users_by_email_and_name,
                                                                                                              authors_updated,
                                                                                                              number_or_projects_to_update,
                                                                                                              users_inserted))

def parse_args(args):
    parser = argparse.ArgumentParser(prog='kedehub',
                                 description='Extract KEDE statistics from Git repositories')
    command_parsers = parser.add_subparsers(dest='subparser_name')

    create_identity_merge_parser(command_parsers)

    return parser.parse_args(args)


def create_identity_merge_parser(command_parsers):
    identity_merge_parser = command_parsers.add_parser('identity-merge', help='Merge identities of existing projects')
    identity_merge_parser.add_argument('-p', '--project', nargs='+',
                                       help='Name of the project which identities to merge')
    identity_merge_parser.add_argument('--verbose', dest='verbose', action='store_true')
    identity_merge_parser.add_argument('--no-verbose', dest='verbose', action='store_false')
    identity_merge_parser.set_defaults(verbose=False)
    identity_merge_parser.set_defaults(func=identity_merge_project)

def Main() -> None:
    # parse the args
    parsed_args = parse_args(sys.argv[1:])
    # call whatever function was selected
    parsed_args.func(parsed_args)

if __name__ == '__main__':
  Main()