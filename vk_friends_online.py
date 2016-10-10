import vk
import getpass

APP_ID = 5662270
ACCESS_TOKEN = 'Mu391hpLUSWD8y0hJorQ'


def get_user_login():
    return input('Введите Ваш логин --> ')


def get_user_password():
    return getpass.getpass('Пароль: ')


def get_online_friends(usr_login, usr_password):
    session = vk.AuthSession(
        app_id=APP_ID,
        access_token=ACCESS_TOKEN,
        user_login=usr_login,
        user_password=usr_password,
        scope='friends'
    )

    api = vk.API(session)
    ids_of_friends_online = api.friends.getOnline()
    online_friends = api.users.get(
        user_ids=', '.join([str(friend_id)
                            for friend_id in ids_of_friends_online])
    )
    return online_friends


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
