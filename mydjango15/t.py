
# 포스팅 : 제목, 내용, 글쓴이

post = ('제목', '내용', '글쓴이')
# 중간에 새로운 것을 끼워넣으면 호출이 꼬임 => 뒤에 append


# namedtuple

from collections import namedtuple

Post = namedtuple('Post', 'title content', 'author_name')
post = Post('제목', '내용', '글쓴이')
post[0], post[1], post[2]
post.title, post.content, post.author_name

def check_content():
    pass


# CapitalCase
class Post:
    # 생성자 __init__
    def __init__(self, title, content, author_name):
        # title = ""  # 지역변수
        self.title = title
        self.content = content
        self.author_name = author_name
    def check_content(self):
        if len(self.content) == 0:
            # error..
            pass

post = Post('제목', '내용', '글쓴이')
post.title
post.content
post.author_name
post.check_content

