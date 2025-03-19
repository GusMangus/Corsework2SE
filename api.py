from flask import Blueprint, jsonify
import logging
import utils


api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename="logs/api.log", format="%(asctime)s [%(levelname)s] %(message)s")


@api_blueprint.route('/api/posts')
def api_posts():
    posts = utils.get_posts_all()
    return jsonify(posts), 200


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id):
    post = utils.get_post_by_pk(post_id)
    return jsonify(post), 200

