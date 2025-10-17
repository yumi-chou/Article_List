from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

comments_dict = {
    1: [
        {"author": "Amanda", "content": "這是第1篇文章的留言1"},
        {"author": "Alex", "content": "這是第1篇文章的留言2"},
    ],
    2: [
        {"author": "Alex", "content": "這是第2篇文章的留言1"},
        {"author": "linda", "content": "這是第2篇文章的留言2"},
        {"author": "tim", "content": "這是第2篇文章的留言3"},
    ],
    3: [
        {"author": "Joe", "content": "這是第3篇文章的留言1"},
        {"author": "Alex", "content": "這是第3篇文章的留言2"},
    ],
    4: [
        {"author": "Sam", "content": "這是第4篇文章的留言1"},
    ],
}

likes_dict = {
    1: [
        {"author": "juuudy", "content": "likes your post"},
        {"author": "krisss", "content": "likes your post"},
        {"author": "micky", "content": "likes your post"},
        {"author": "tim", "content": "likes your post"},
        {"author": "patty", "content": "likes your post"},
    ],
    2: [
        {"author": "Joe", "content": "likes your post"},
        {"author": "Sam", "content": "likes your post"},
        {"author": "kris", "content": "likes your post"},
        {"author": "juuudy", "content": "likes your post"},
        {"author": "krisss", "content": "likes your post"},
        {"author": "micky", "content": "likes your post"},
    ],
    3: [
        {"author": "tim", "content": "likes your post"},
        {"author": "patty", "content": "likes your post"},
    ],
    4: [
        {"author": "mike", "content": "likes your post"},
        {"author": "mickyyy", "content": "likes your post"},
    ],    
}

@app.get("/api/comments/{article_id}")
def get_comments(article_id: int):
    return comments_dict.get(article_id, [])


@app.get("/api/likes/{article_id}")
def get_likes(article_id: int):
    return likes_dict.get(article_id, [])
