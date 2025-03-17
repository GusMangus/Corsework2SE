from utils import get_posts_all, get_comments_by_post_id, load_comments, get_post_by_pk, get_posts_by_user, \
    search_for_posts

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}



class TestUtils:

    def test_get_posts_all(self):
        """ Проверяем получение всех постов"""
        posts = get_posts_all()
        assert type(posts) == list
        assert len(posts) > 0
        assert set(posts[0].keys()) == keys_should_be

    def test_get_posts_by_user(self):
        """ Проверяем получение поста"""
        posts = get_posts_by_user('leo')
        assert type(posts) == list
        for post in posts:
            assert post["poster_name"] == 'leo'
            assert set(post.keys()) == keys_should_be

    def test_get_comments_by_post_id(self):
        """ Проверяем получение комментария"""
        comments = get_comments_by_post_id(1)
        assert type(comments) == list
        for comment in comments:
            assert comment[0] == 'jlia' or 'hanna'

    def test_search_for_posts(self):
        """ Проверяем поиск поста"""
        post = search_for_posts('тарелка')
        assert type(post) == list
        for p in post:
            assert p['pk'] == 1
            assert set(p.keys()) == keys_should_be

    def test_get_post_by_pk(self):
        """ Проверяем получение поста"""
        p = get_post_by_pk(1)
        assert p['pk'] == 1
        assert set(p.keys()) == keys_should_be
        assert type(p) == dict


