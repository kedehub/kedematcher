from kedehub_client import get_sync_apis
from kedehub.git.git_utility import get_name, get_email

def save_new_author(author_line):
    name = get_name(author_line)
    email = get_email(author_line)
    apis = get_sync_apis()
    author = apis.author_api.save_new_author(author_line, name, email)
    return author

def build_author_map(project_name):
    apis = get_sync_apis()
    return apis.author_api.build_author_map(project_name)

def assign_author_to_user_profile(author):
    apis = get_sync_apis()
    authors_updated = apis.author_api.update_author_to_user_profile(author)
    return authors_updated