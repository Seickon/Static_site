import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    copy = old_nodes.copy()
    new_nodes = []
    for node in copy:
        temporary_strings = []
        temporary_nodes = []
        temporary_strings.extend(node.text.split(delimiter, 2))
        if len(temporary_strings) == 2:
            raise Exception(f"Ending {delimiter} missing")
        if len(temporary_strings) == 3:
            temporary_nodes.append(TextNode(temporary_strings[0], node.text_type))
            temporary_nodes.append(TextNode(temporary_strings[1], text_type))
            temporary_nodes.append(TextNode(temporary_strings[2], node.text_type))
        else:
            temporary_nodes.append(node)
        new_nodes.extend(temporary_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    retrun_list = []
    for node in old_nodes:
        temporary_strings = []
        text_and_link = extract_markdown_images(node.text)
        temporary_strings.extend(re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text))
        retrun_list.append(TextNode(temporary_strings[0], node.text_type))
        i = 0
        for image in text_and_link:
            temporary_nodes = []
            i += 3
            temporary_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            temporary_nodes.append(TextNode(temporary_strings[i], node.text_type))
            retrun_list.extend(temporary_nodes)
        deletion = 0
        for Node in retrun_list:
            if Node.text == "":
                del retrun_list[deletion]
            deletion += 1
    return retrun_list

def split_nodes_link(old_nodes):
    retrun_list = []
    for node in old_nodes:
        temporary_strings = []
        text_and_link = extract_markdown_links(node.text)
        if len(text_and_link) == 0:
            retrun_list.append(node)
        else:
            temporary_strings.extend(re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text))
            retrun_list.append(TextNode(temporary_strings[0], node.text_type))
            i = 0
            for image in text_and_link:
                temporary_nodes = []
                i += 3
                temporary_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
                temporary_nodes.append(TextNode(temporary_strings[i], node.text_type))
                retrun_list.extend(temporary_nodes)
            deletion = 0
            for Node in retrun_list:
                if Node.text == "":
                    del retrun_list[deletion]
                deletion += 1
    return retrun_list

def extract_markdown_images(text):
    #return re.findall(r"\!\[(.?*)\]\((.?*)\)", text)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    #return re.findall(r"\[(.?*)\]\((.?*)\)", text)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    Node = TextNode(text, TextType.TEXT)
    Node = split_nodes_delimiter([Node], "**", TextType.BOLD)
    Node = split_nodes_delimiter(Node, "_", TextType.ITALIC)
    Node = split_nodes_delimiter(Node, "`", TextType.CODE)
    Node = split_nodes_image(Node)
    Node = split_nodes_link(Node)
    return Node