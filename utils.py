import json
from config import post_path, comments_path



def get_posts_all() -> list[dict]:
    """возвращает посты"""
    with open(post_path, 'r', encoding="utf-8") as f:
        return json.load(f)


def load_comments() -> list[dict]:
    with open(comments_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user) -> list[dict]:
    """возвращает посты определенного пользователя"""
    result = []
    for item in get_posts_all():
        if item['poster_name'].lower() == user.lower():
            result.append(item)
    if len(result) == 0:
        return ValueError and f'У пользователя нет постов'
    return result


def get_comments_by_post_id(post_id) -> list[dict]:
    """возвращает комментарии определенного поста"""
    result = []
    for comment in load_comments():
        if comment['post_id'] == post_id:
            result.append((comment['commenter_name'], comment['comment']))
    return result


def search_for_posts(query) -> list[dict]:
    """возвращает список постов по ключевому слову"""
    posts = []
    for item in get_posts_all():
        if query in item['content'].lower():
            posts.append(item)
    return posts


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    for item in get_posts_all():
        if item['pk'] == pk:
            return item



