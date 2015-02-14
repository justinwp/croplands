from gfsad.exceptions import Unauthorized
from gfsad.utils.s3 import upload_photo
from gfsad.tasks.records import get_ndvi
from gfsad.auth import allowed_roles, verify_role, load_user


def api_roles(role):
    def wrapper(*args, **kwargs):
        if not allowed_roles(role):
            raise Unauthorized()

    return wrapper


def check_for_photo(data=None, **kwargs):
    pass


def after_post_record():
    get_ndvi.apply()


def add_user_to_posted_data(data=None, **kwargs):
    """
    Appends user_id to data if user is not none.
    :param data: data from api endpoint
    :param kwargs:
    :return: None
    """
    user = load_user()
    if user is 'anonymous':
        return

    data['user_id'] = user.id

    #TODO Improve method of applying user_id to sub models
    # perhaps using get_related_model? looping through entities of array?
    if 'records' in data:
        for record in data['records']:
            record['user_id'] = user.id

    if 'photos' in data:
        for photo in data['photos']:
            photo['user_id'] = user.id


def remove_relations(data=None, **kwargs):
    """
    Removes all relations from patched data.
    :param data:
    :param kwargs:
    :return: None
    """
    keys_to_delete = []
    for key, val in data.iteritems():
        if type(data[key]) is list:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del data[key]