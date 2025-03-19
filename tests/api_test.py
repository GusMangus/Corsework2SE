from main import app

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_get_posts_all():
    """ Проверяем получение всех постов"""
    response = app.test_client().get('/api/posts', follow_redirects=True)
    assert type(response.json) == list, "Получен не список"
    assert set(response.json[0].keys()) == keys_should_be, "Ключи не совпадают"


def test_api_post_by_pk():
    """ Проверяем получение поста"""
    response = app.test_client().get('/api/posts/1', follow_redirects=True)
    assert response.status_code == 200
    assert response.mimetype == "application/json", "Получен не JSON"
    assert type(response.json) == dict, "Получен не словарь"
    assert set(response.json.keys()) == keys_should_be, "Ключи не совпадают"
