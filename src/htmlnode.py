class HTMLNode:
    def __init__ (self = None, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props # dictionary of key value pairs

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        string = ""
        if self.props == None or self.props != {}:
            for key, value in self.props.items():
                string = string + key + '="' + value + '" '
        
        string = string.strip()
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"