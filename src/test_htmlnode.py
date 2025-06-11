import unittest

from htmlnode import *

class TestTo_html(unittest.TestCase):
    def tests(self):
        test = HTMLNode()
        with self.assertRaises(NotImplementedError):
            test.to_html()

class TestProps_to_html(unittest.TestCase):
    def tests(self):
        props= {
                "href": "https://www.google.com",
                "target": "_blank",
                }
        test = HTMLNode(None, None, None, props)
        print(test.props_to_html())
        self.assertMultiLineEqual(test.props_to_html() , ' href="https://www.google.com" target="_blank"')

class TestPrint(unittest.TestCase):
    def tests(self):
        test = HTMLNode("p", "Ein Sehr Crativer TEst der hier Steht")
        string = "Tag: p, Value: Ein Sehr Crativer TEst der hier Steht, Children: None, Props: None"
        self.assertMultiLineEqual(str(test), string)


class TestLeafes(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        Leaf = LeafNode("u", "Klicky Linki dingi!", {"href": "https://www.google.com"})
        string = '<u href="https://www.google.com">Klicky Linki dingi!</u>'
        self.assertMultiLineEqual(Leaf.to_html(), string)
    
    def test_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_no_Value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


class TestParrentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    