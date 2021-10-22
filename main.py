from flask import Flask, render_template
from post import Post
import requests

posts = requests.get('https://api.npoint.io/ed99320662742443cc5b').json()
post_objects = []
for post in posts:
    post_obs = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obs)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post

    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
