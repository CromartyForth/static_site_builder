class HTMLNode:
    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props # dictionary of key value pairs

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        string = ""
        if self.props == None or self.props == {}:
            return string
        
        for key, value in self.props.items():
                string = string + key + '="' + value + '" '
        string = string.strip()
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            # leaf node must have a value
            raise ValueError("LeafNode must have a value")
        
        if self.tag == None:
            # value returned as raw text
            return f"{self.value}"
        
        if self.props:
            # render html tag with props
            props = self.props_to_html()
            return f"<{self.tag} {props}>{self.value}</{self.tag}>"
        
        # render html tag
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == "" or self.tag is None:
            raise ValueError("tag must have a value")
        
        if self.children == [] or self.children is None:
            raise ValueError("Parent must have a child value")
        
        # itterate over children
        child_strings = ""
        for child in self.children:
            #child could be parentNode or leafNode each has it's own method
            child_strings = child_strings + child.to_html()

        # generate html for parent add result of itterating children
        if self.props:
            # render html tag with props
            props = self.props_to_html()
            return f"<{self.tag} {props}>{child_strings}</{self.tag}>"
        
        # render html tag
        return f"<{self.tag}>{child_strings}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
            


        

