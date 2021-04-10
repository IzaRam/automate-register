import requests
from generate_users import list_users


def get_all_users():
    r = requests.get("http://127.0.0.1:5000/users")
    print(r.json())


def get_users_by_id(user_id):
    r = requests.get("http://127.0.0.1:5000/user/" + str(user_id))
    print(r.json())


def post_all_generated_users():
    for user in list_users:
        r = requests.post("http://127.0.0.1:5000/users", json=user)
        print(r)


def post_new_user(user):
    r = requests.post("http://127.0.0.1:5000/users", json=user)
    print(r)


def update_user_by_id(user_id, user):
    r = requests.put("http://127.0.0.1:5000/user/edit/" + str(user_id), json=user)
    print(r)


def delete_user_by_id(user_id):
    r = requests.delete("http://127.0.0.1:5000/user/del/" + str(user_id))
    print(r)
