from pydantic import EmailStr

from kedehub_client import get_sync_apis

def create_new_user(user):
    new_user = get_sync_apis().user_api.post_create_new_user(user)
    return new_user
