 HEAD
# app.py
from flask import Flask
import config

app = Flask(__name__)

# config.py에서 설정을 로드
app.config.from_object(config.Config)

@app.route('/')
def index():
    return 'Hello, Flask
from flask import Flask, render_template, request, redirect

# Flask 애플리케이션 초기화 (이 부분이 없으면 app을 사용할 수 없어요)
app = Flask(__name__)

# 예시 데이터 (실제로는 데이터베이스에서 가져와야 합니다)
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:id>')
def post_detail(id):
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        return render_template('post_detail.html', post=post)
    else:
        return "Post not found", 404

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        new_id = len(posts) + 1
        new_post = {
            "id": new_id,
            "title": request.form['title'],
            "content": request.form['content']
        }
        posts.append(new_post)
        return redirect('/')
    return render_template('post_form.html')

@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        if request.method == 'POST':
            post['title'] = request.form['title']
            post['content'] = request.form['content']
            return redirect(f'/posts/{id}')
        return render_template('post_form.html', post=post)
    else:
        return "Post not found", 404

@app.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        posts.remove(post)
        return redirect('/')
    else:
        return "Post not found", 404

# Flask 애플리케이션 실행
 99c0e43 (Initial commit)
if __name__ == '__main__':
    app.run(debug=True)

