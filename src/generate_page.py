import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    markdown = from_file.read()
    from_file.close()
    template_file = open(template_path)
    template = template_file.read()
    template_file.close()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown) 
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    path = os.path.dirname(dest_path)
    os.makedirs(path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(html)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = "/"):
    contets = os.listdir(dir_path_content)
    for dir in contets:
        content = os.path.join(dir_path_content, dir)
        dest = os.path.join(dest_dir_path, dir)
        if os.path.isfile(content):
            dest = dest.replace(".md", ".html")
            generate_page(content, template_path, dest, basepath)
        else:
            os.makedirs(dest, exist_ok=True)
            generate_pages_recursive(content, template_path, dest, basepath)