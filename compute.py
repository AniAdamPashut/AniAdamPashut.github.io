import os

posts = os.listdir('./markdowns')

f = open('base.html')
temp = f.read()
f.close()

for post in posts:
    with open('./markdowns/' + post) as f:
        content = f.read()
        t = temp.replace('<replace-title-header>', post[:-3])
        t = t.replace('<replace-title-h1>', post[:-3])
        t = t.replace('<replace-content>', content)
        out = open('posts/' + post[:-3] + '.html', 'w')
        out.write(t)
        out.close()

atags = [f'<a href="./posts/{post[:-3]}">{post[:-3]}</a>' for post in posts]
atags = '\n'.join(atags)
with open('index.html') as f:
    content = f.read()

content = content.replace('<replace-this-with-links-to-posts>', atags)
with open('index.html', 'w') as f:
    f.write(content)