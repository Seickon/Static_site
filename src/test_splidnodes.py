import unittest
from textnode import *
from splitnodes import *

class TestSplitNodes(unittest.TestCase):
    def test_regular(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
        expectet = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expectet)

    def test_splid_end_of_string(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
        expectet = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expectet)

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD) 
        expectet = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expectet)

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC) 
        expectet = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expectet)

    def test_split_start_of_string(self):
        node = TextNode("`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
        expectet = [
            TextNode("", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expectet)

class TestExtractionFunctions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestImagesAndLinkSplz(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://www.boot.dev/dashboard) and another [second link](https://regexr.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev/dashboard"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://regexr.com"),
            ],
            new_nodes,
        )

    def test_split_links_beginning(self):
        node = TextNode(
            "[link](https://www.boot.dev/dashboard) and another [second link](https://regexr.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.boot.dev/dashboard"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://regexr.com"),
            ],
            new_nodes,
        )

class TestTextToTextnodes(unittest.TestCase):
    def test_normal(self):
        Text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        Expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]
        self.assertEqual(text_to_textnodes(Text), Expected)

    def test_reverse_direction(self):
        Text = "This is [link](https://boot.dev) with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) word and a `code block` and an _italic_ and a **text**"
        Expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    ]
        self.assertEqual(text_to_textnodes(Text), Expected)




