class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_list = []
        for i in self.props:
            # i = key, self.props[i] = value
            props_list.append(f" {i}=\"{self.props[i]}\"")
        return "".join(props_list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode does not have a value")
        if self.tag == None:
            return self.value
        leaf_html = ""
        leaf_html += f"<{self.tag}>"

# ^^^ PICK BACK UP HERE ^^^
# https://www.boot.dev/assignments/ac96cd47-bf01-4599-8291-cd69534f288f
