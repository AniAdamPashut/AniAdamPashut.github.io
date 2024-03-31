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

for file in files:
    html = pypandoc.convert_file(f'{md_folder}\\{file}', 'html', extra_args=['--wrap=none'])
    full_content = base.replace("<CONTENT_GOES_IN_HERE/>", html)

    with open(f'{posts_folder}\\{file[:-3]}.html', 'w', encoding='utf-8') as f:
        f.write(full_content.encode('utf-8').replace(b'\r\n', b'\n').decode())