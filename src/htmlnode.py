
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        list_strings = []
        for key, value in self.props.items():
            list_strings.append(f' {key}="{value}"')
        return "".join(list_strings)
    
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is necessary")
        if self.children == None:
            raise ValueError("Children are not optional")
        string = f"<{self.tag}>"
        for child in self.children:
            string += child.to_html()
        string += f"</{self.tag}>"
        return string
    