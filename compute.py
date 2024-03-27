import os

posts = os.listdir('./markdowns')

for file in os.listdir('./posts'):
    file_path = os.path.join('./posts', file)
    if os.path.isfile(file_path) and file_path.endswith('.html'):
        os.remove(file_path)

f = open('base.html')
temp = f.read()
f.close()

for post in posts:
    with open('./markdowns/' + post) as f:
        if not post.endswith('.md'):
            continue
        
        content = f.read()
        t = temp.replace('<replace-title-header>', post[:-3])
        t = t.replace('<replace-title-h1>', post[:-3])
        t = t.replace('<replace-content>', content)
        out = open('posts/' + post[:-3] + '.html', 'w')
        out.write(t)
        out.close()

atags = [f'<a href="./posts/{post[:-3]}">{post[:-3]}</a>' for post in posts]
atags = '\n'.join(atags)
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="styles.css"/>
    <title>benAmi spews stuff</title>
</head>
<body>
    <h3>Posts</h3>
    <ul id="posts">
        <replace-this-with-links-to-posts>
    </ul>
</body>
</html>
"""
content = content.replace('<replace-this-with-links-to-posts>', atags)
with open('index.html', 'w') as f:
    f.write(content)