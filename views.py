from flask import Flask, Blueprint, render_template, request

import utils

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/post/<int:pk>/')
def open_post(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    comments_count = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_count=comments_count)

@main_blueprint.route('/search')
def search():
    s = request.args.get("s")
    posts = utils.search_for_posts(s)
    posts_count = len(posts)
    return render_template('search.html', posts=posts, posts_count=posts_count, query=s)

@main_blueprint.route('/user/<username>')
def open_feed(username):
    post = utils.get_posts_by_user(username)
    posts_count = len(post)
    return render_template('user-feed.html', post=post, posts_count=posts_count)
