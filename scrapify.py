
import praw
import prawcore
import sqlite3
##########################
reddit = praw.Reddit(
    client_id="VoVzkNE77Sqxf6SeT4CShg",
    client_secret="6HPRq0mfA3IMHQFx_frZrCLOI6Ulag",
    user_agent="Web_Dev_24",
)
######

conn = sqlite3.connect('reddit_posts_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        post_id TEXT UNIQUE,
        author TEXT,
        url TEXT,
        created_utc INTEGER,
        upvotes INTEGER,
        comment_count INTEGER
    )
''')

conn.commit()


def fetch_top_posts(subreddit, time_filter='all', limit=100):
    top_posts = subreddit.top(time_filter=time_filter, limit=limit)
    return list(top_posts)

def display_post_info(post):
    print("Title - ", post.title)
    print("ID - ", post.id)
    print("Author - ", post.author)
    print("URL", post.url)
    print("Created on - ", post.created_utc)
    print("Upvotes - ", post.score)
    print("Comment count - ", post.num_comments)
    print("\n")

def store_post_in_database(conn, post):
    cursor = conn.cursor()

    # check if post with the same ID already exists
    cursor.execute("SELECT * FROM posts WHERE post_id = ?", (post.id,))
    existing_post = cursor.fetchone()

    if existing_post is None:
        cursor.execute("""
            INSERT INTO posts (title, post_id, author, url, created_utc, upvotes, comment_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            post.title,
            post.id,
            str(post.author),
            post.url,
            post.created_utc,
            post.score,
            post.num_comments
        ))
        conn.commit()
    else:
        print(f"Post with ID {post.id} already exists in database")


def fetch_posts_comments(conn, fetched_posts):
    # fetch comments from post using Chosen ID
    post_id = input("Enter your choice of Post ID - ")
    if post_id:
        selected_post = next((post for post in fetched_posts if post.id == post_id), None)
        if selected_post:
            try:
                comments = selected_post.comments

                for comment in comments[:5]:
                    print("Comment printing....")
                    print("Comment Body - ", comment.body)
                    print("Author - ", comment.author)
                    print("\n")

            except prawcore.exceptions.NotFound:
                print(f"Post with ID {post_id} not found")
            except praw.exceptions.PRAWException as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")



def main():
    subreddit_name = input("Subreddit Name ? - ")
    subreddit = reddit.subreddit(subreddit_name)
    
    fetched_posts = []

    #fetch more posts by iterating through multiple pages
    for page_number in range(1, 5):
        print(f"Page {page_number} of {subreddit}")

        #fetch n number of posts per page
        posts = fetch_top_posts(subreddit, limit=5 * page_number)

        for post in posts:
            fetched_posts.append(post)
            display_post_info(post)
            store_post_in_database(conn, post)

        # fetch and display comments from post based on user input
        fetch_posts_comments(conn, fetched_posts=fetched_posts)


if __name__ == "__main__":
    main()
    conn.close()