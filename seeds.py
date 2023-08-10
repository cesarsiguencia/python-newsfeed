from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
# db.add_all([
#   User(username='CesarSig', email='cesar@gmail.com"', password='abcd1234'),
#   User(username='Samantha', email='sam@gmail.com"', password='1234abcd'),
#   User(username='Anna', email='anna@gmail.com', password='password'),
# ])
# db.commit()

db.add(
  User(username='CesarSig', email='cesar@gmail.com"', password='abcd1234')
)
db.commit()

db.add(
  User(username='Samantha', email='sam@gmail.com"', password='1234abcd')
)
db.commit()

db.add(
  User(username='Anna', email='anna@gmail.com', password='password')
)
db.commit()

# insert posts
db.add_all([
  Post(title="My first post", post_url="https://www.apple.com/", user_id=1),
  Post(title="Her first post", post_url="https://www.youtube.com/", user_id=2),
  Post(title='Please checkout my portfolio', post_url="https://cesarsiguencia.github.io/my-react-portfolio/", user_id=1),
  Post(title='Anyone know React well and can help me?', post_url='https://www.reactenlightenment.com/', user_id=3),
  Post(title='Some technical interview advice I found!', post_url='https://perscholas.org/news/how-to-land-your-first-job-in-tech-resume-and-interview-tips/?utm_source=google&utm_medium=ad_grant&utm_campaign=blog&utm_term=interviewing%20tips&utm_campaign=Per+Scholas:+Awareness&utm_source=adwords&utm_medium=ppc&hsa_acc=7812736465&hsa_cam=16572465740&hsa_grp=132888643365&hsa_ad=587608286116&hsa_src=g&hsa_tgt=kwd-21418711&hsa_kw=interviewing%20tips&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwldKmBhCCARIsAP-0rfzCJFHtxWKUzBMJ5vuhLeklfhKjXfCysjyLlJ7DOp5QW1mscQ-nNVYaAuSnEALw_wcB', user_id=2)
])
db.commit()

# insert comments
db.add_all([
  Comment(comment_text="Congratulations on your first post!", user_id=2, post_id=1),
  Comment(comment_text="Jealous of your portfolio! :)", user_id=2, post_id=3),
  Comment(comment_text="Teach me how to do this!", user_id=3, post_id=3),
  Comment(comment_text='I can help! Message me', user_id=1, post_id=4),
  Comment(comment_text='Thanks for sharing this!', user_id=2, post_id=5)
])
db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=2, post_id=1),
  Vote(user_id=2, post_id=3),
  Vote(user_id=3, post_id=3),
  Vote(user_id=1, post_id=5),
  Vote(user_id=2, post_id=5),
  Vote(user_id=2, post_id=4),
])
db.commit()

db.close()
