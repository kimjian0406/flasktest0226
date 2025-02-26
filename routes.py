# routes.py

from flask import Blueprint, request, jsonify

# Blueprint를 사용하여 라우트를 분리합니다.
posts_blueprint = Blueprint('posts', __name__)

# 모든 게시글 조회
@posts_blueprint.route('/posts', methods=['GET'])
def get_posts():
    posts = [
        {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
        {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'}
    ]
    return jsonify(posts)

# 특정 ID의 게시글 조회
@posts_blueprint.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    posts = [
        {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
        {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'}
    ]
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404

# 새 게시글 생성
@posts_blueprint.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = 3  # 예시로 id 3번으로 설정
    return jsonify(new_post), 201

# 특정 ID의 게시글 수정
@posts_blueprint.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    updated_post = request.get_json()
    posts = [
        {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
        {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'}
    ]
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        post.update(updated_post)
        return jsonify(post)
    else:
        return jsonify({'message': 'Post not found'}), 404

# 특정 ID의 게시글 삭제
@posts_blueprint.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    posts = [
        {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
        {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'}
    ]
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        posts.remove(post)
        return jsonify({'message': f'Post with id {id} has been deleted'}), 200
    else:
        return jsonify({'message': 'Post not found'}), 404
