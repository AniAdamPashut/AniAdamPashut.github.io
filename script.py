import os
import pypandoc

folder_path = r"C:\Users\mineb\blog\aniadampashut.github.io"
os.chdir(folder_path)

md_folder = r".\markdown"
posts_folder = r".\posts"
files = os.listdir(md_folder)
posts = os.listdir(posts_folder)

with open(r'.\base.html') as f:
    base = f.read()

for post in posts:
    os.remove(f'{posts_folder}\\{post}')

index_updating = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>benAmi spews stuff</title>
    <link href='https://fonts.googleapis.com/css?family=Open Sans' rel='stylesheet'>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <article>
        <h1>The shitposting website benami wrote for suffering</h1>
        <h3>Posts</h3>
        <ul id="posts">
            <LIST_GOES_HERE/>
        </ul>
    </article>
    <footer>
        This website is written by the simplest of men for the simple man. Made by <a href="https://open.spotify.com/track/1F5zcJWVYelsmk1493aNm1?si=bf3bb36860af4569" target="_blank">AniAdamPashut</a> also known as benAmi.
    </footer>
</body>
</html>"""

post_list = []

for file in files:
    if not file.endswith('.md'):
        continue
    html = pypandoc.convert_file(f'{md_folder}\\{file}', 'html', extra_args=['--wrap=none'])
    full_content = base.replace("<CONTENT_GOES_IN_HERE/>", html)

    out = f'{posts_folder}\\{file[:-3]}.html'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(full_content.encode('utf-8').replace(b'\r\n', b'\n').decode())

    list_item = f'<li><a href="{out}">{file[:-3]}</a></li>'
    post_list.append(list_item)

index_file = index_updating.replace('<LIST_GOES_HERE/>', '\n'.join(post_list))
with open('index.html', 'w') as f:
    f.write(index_file)