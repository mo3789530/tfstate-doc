import markdown


def md_to_html(md_txt: str) -> str:
    md = markdown.Markdown(extensions=['tables'])
    return md.convert(md_txt)


def save(output: str, html: str):
    with open(output, mode='w') as f:
        f.write(html)