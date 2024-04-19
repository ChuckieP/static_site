class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        for i in self.props:
            # i = key, self.props[i] = value
            props_list.append(f" {i}=\"{self.props[i]}\"")
        return "".join(props_list)
