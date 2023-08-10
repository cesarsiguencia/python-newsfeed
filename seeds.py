from models import User, Post, Comment, Vote
from db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='CesarSig', email='cesar@gmail.com"', password='abcd1234'),
  User(username='Samantha', email='sam@gmail.com"', password='1234abcd'),
  User(username='Anna', email='anna@gmail.com', password='password'),
])
db.commit()


# insert posts
db.add_all([
  Post(title="My first post", post_url="https://www.apple.com/", user_id=1),
  Post(title="Her first post", post_url="https://www.youtube.com/", user_id=2),
  Post(title='Please checkout my portfolio', post_url="https://cesarsiguencia.github.io/my-react-portfolio/", user_id=1)
])
db.commit()

# insert comments
db.add_all([
  Comment(comment_text="Congratulations on your first post!", user_id=2, post_id=1),
  Comment(comment_text="Jealous of your portfolio! :)", user_id=2, post_id=3),
  Comment(comment_text="Teach me how to do this!", user_id=3, post_id=3),
])
db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=2, post_id=1),
  Vote(user_id=2, post_id=3),
  Vote(user_id=3, post_id=3)
])
db.commit()

db.close()