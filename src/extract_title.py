

def extract_title(markdown):
    markdown.strip()
    if markdown.startswith("# "):
        return markdown.split("# ", 1)[1].strip()
    raise Exception("No title found")