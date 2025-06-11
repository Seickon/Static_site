from blocks import *
from htmlnode import *
from splitnodes import text_to_textnodes
from textnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(blocks_to_html(block))
    return ParentNode("div", children)


def blocks_to_html(block):
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block))
        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(block))
        case BlockType.CODE:
            return ParentNode("pre", [text_node_to_html_node(TextNode(block[4:-3:], TextType.CODE))])
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", unordered_list_children(block))
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", ordered_list_children(block))
        case BlockType.HEADING:
            return html_heading_optimised(block)

def text_to_children(text=""):
    text = text.replace("\n", " ")
    if ">" in text:
        text = text.replace("> ", "")
    nodes = text_to_textnodes(text)
    leafs = []
    for node in nodes:
        leafs.append(text_node_to_html_node(node))
    return leafs

def unordered_list_children(block):
    elements = block.strip().split("- ")
    html = []
    for element in elements:
        if element.strip():
            html.append(ParentNode("li", text_to_children(element.strip())))
    return html

def ordered_list_children(block):
    lines = block.strip().split('\n')
    html = []
    for line in lines:
        if line.strip():
            if '. ' in line:
                content = line.split('. ', 1)[1]
                html.append(ParentNode("li", text_to_children(content)))
    return html

def html_heading(block=""):
    if block.startswith("###### "):
        return ParentNode("h6", text_to_children(block[6:]))
    if block.startswith("##### "):
        return ParentNode("h5", text_to_children(block[5:]))
    if block.startswith("#### "):
        return ParentNode("h4", text_to_children(block[4:]))
    if block.startswith("### "):
        return ParentNode("h3", text_to_children(block[3:]))
    if block.startswith("## "):
        return ParentNode("h2", text_to_children(block[2:]))
    if block.startswith("# "):
        return ParentNode("h1", text_to_children(block[1:]))
    
def html_heading_optimised(block=""):
    for i in range(6, 0, -1): 
        if block.startswith("#" * i + " "):
            return ParentNode(f"h{i}", text_to_children(block[i+1:]))