print(
    "My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s And now thinks he's a %s."
    % ("roast beef", "ham", "head", "clam")
)

# sol에서 쓴 방법(ipython에서 할 때 단계별로 하는 방법)
poem = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.
"""
# poem을 먼저 지정해두고 % 뒤에 들어갈 리스트를 args라는 이름으로 만들어줌
args = ("roast beef", "ham", "head", "clam")
print(poem % args)
