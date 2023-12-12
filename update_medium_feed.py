import feedparser

def get_latest_medium_post(url, limit=5):
    feed = feedparser.parse(url)
    return [(x.title, x.link) for x in feed.entries[:limit]]

def update_readme(posts, readme_path='README.md'):
    start_marker = '<!--AUTO: MEDIUM-->'
    end_marker = '<!--AUTO: MEDIUM_END-->'
    new_content = '\n' + '\n'.join(f'- [{title}]({link})' for title, link in posts) + '\n'

    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Find the start and end indices
    start_index = next(i for i, line in enumerate(lines) if start_marker in line)
    end_index = next(i for i, line in enumerate(lines) if end_marker in line)

    # Replace the content between markers, including new lines at start and end
    updated_lines = lines[:start_index + 1] + [new_content] + lines[end_index:]
    
    with open(readme_path, 'w') as file:
        file.writelines(updated_lines)

rss_url = 'https://medium.com/feed/@enebin'
latest_posts = get_latest_medium_post(rss_url)
update_readme(latest_posts)
