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