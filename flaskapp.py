from flask import Flask, render_template, request
from scrapify import fetch_top_posts, store_post_in_database, fetch_posts_comments

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_posts', methods=['POST'])
def fetch_posts():
    subreddit = request.form['subreddit']
    posts = fetch_top_posts(subreddit)
    for post in posts:
        store_post_in_database(post)
    return 'Posts fetched and stored successfully!'

@app.route('/fetch_comments', methods=['POST'])
def fetch_comments():
    post_id = request.form['post_id']
    comments = fetch_posts_comments(post_id)
    return render_template('comments.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
