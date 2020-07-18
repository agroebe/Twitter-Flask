class Tweet():

    def __init__(self, contents):
        self.contents = contents

    def write(self, g):
        vertex = g.addV('tweet')
        vertex.property('contents', self.contents)
        result = vertex.next()
        return result.id