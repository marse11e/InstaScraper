import os
import json
import csv
import string
from random import randint
from time import sleep
from pprint import pprint as pp
from datetime import datetime

import instaloader
from instaloader import Profile

from settings import USER, PASSWORD

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session (1 вариант входа)
# L.interactive_login(USER)  # Ввести пароль вручную
# Загрузить сессию, созданную с `instaloader -l USERNAME`
# L.load_session_from_file(
#     USER, filename='session-file/session-marselle_naz'
# )

# Login and save session (2 вариант входа)
L.login(USER, PASSWORD)  # Ввести логин и пароль
L.save_session_to_file(filename='session-file/')  # Сохранить сессию в файл


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        pass


def sanitize_file_name(file_name: str) -> str:
    new_file_name = file_name.translate(
        str.maketrans('', '', string.punctuation))
    return new_file_name


# ----------------------------------------------------------------
# Используйте это как последнее средство, иначе мут на час
def has_highlight_reels(profile: Profile) -> bool:
    return profile.has_highlight_reels


def has_viewable_story(profile: Profile) -> bool:
    return profile.has_viewable_story


def has_public_story(profile: Profile) -> bool:
    return profile.has_public_story


def has_blocked_viewer(profile: Profile) -> bool:
    return profile.has_blocked_viewer


def has_requested_viewer(profile: Profile) -> bool:
    return profile.has_requested_viewer
# ----------------------------------------------------------------


def information_profile(profile: Profile) -> dict:

    data = {
        'userid': profile.userid,
        'username': profile.username,
        'full_name': profile.full_name,
        'mediacount': profile.mediacount,
        'followers': profile.followers,
        'followees': profile.followees,
        'biography': profile.biography,
        'biography_hashtags': profile.biography_hashtags,
        'biography_mentions': profile.biography_mentions,
        'business_category_name': profile.business_category_name,
        'blocked_by_viewer': profile.blocked_by_viewer,
        'followed_by_viewer': profile.followed_by_viewer,
        'follows_viewer': profile.follows_viewer,
        'requested_by_viewer': profile.requested_by_viewer,
        'igtvcount': profile.igtvcount,
        'is_business_account': profile.is_business_account,
        'is_private': profile.is_private,
        'is_verified': profile.is_verified,
        'external_url': profile.external_url,
        'profile_pic_url': profile.profile_pic_url,
        'profile_pic_url_no_iphone': profile.profile_pic_url_no_iphone,
    }

    file_name = sanitize_file_name(profile.username)

    with open(f'source/json/{file_name}.json', 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    with open(f'source/csv/{file_name}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

    return (f'Данные профиля сохранены.\n'f'Путь: source/json/{file_name}.json\n'f'Путь: source/csv/{file_name}.csv')


def get_profile_posts(profile: Profile) -> None:
    posts = profile.get_posts()

    post_info = {}

    count = 0
    for post in posts:
        L.download_post(post, target=f'{sanitize_file_name(profile.username)}')
        count += 1

        post_info['post_is_owner_id'] = post.owner_id
        post_info['post_profile'] = post.profile
        post_info['post_owner_username'] = post.owner_username
        post_info['post_owner_profile'] = post.owner_profile.full_name
        post_info['post_media_type'] = post.typename
        post_info['post_caption'] = post.caption
        post_info['post_likes'] = post.likes
        post_info['post_comments'] = post.comments
        post_info['post_date'] = str(post.date)
        post_info['post_location'] = post.location
        post_info['post_tagged_users'] = post.tagged_users
        post_info['post_is_video'] = post.is_video
        post_info['post_video_url'] = post.video_url
        post_info['post_is_pinned'] = post.is_pinned
        post_info['post_accessibility_caption'] = post.accessibility_caption
        post_info['post_url'] = post.url
        post_info['info_comments'] = []

        try:
            # Если не авторизованы не работает get_comments
            comments = post.get_comments()

        except:
            post_info['info_comments'].append({'error-auth': 'Не удалось получить комментарии (Не авторизованы.)'})

        else:
            for comment in comments:
                post_info['info_comments'].append({
                    'comment_owner_username': comment.owner.username,
                    'comment_text': comment.text,
                    'comment_likes': comment.likes_count,
                    'comment_date': str(comment.date),
                })

        with open(f"source/posts/{sanitize_file_name(profile.username)}_{post.shortcode}.json", 'w') as f:
            json.dump(post_info, f, indent=4, ensure_ascii=False)

        post_info.clear()
        print(f'Скачано {count} постов')
        # break
        sleep(randint(10, 20))

    return f'Скачано {count} постов'


def main():
    username = '_karina_sarisunova' # < Тут пишете имя пользователя инстаграм
    profile = instaloader.Profile.from_username(L.context, username)
    print(information_profile(profile))
    # print(get_profile_posts(profile))


if __name__ == '__main__':
    os.system('clear')
    main()
