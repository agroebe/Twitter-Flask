class User():

    def __init__(self, username, password, display_name, join_date, bio):
        self.username = username
        self.password = password
        self.display_name = display_name
        self.join_date = join_date
        self.bio = bio

    def write(self, g):
        vertex = g.addV('user')
        vertex.property('username', self.username)
        vertex.property('password', self.password)
        vertex.property('display_name', self.display_name)
        vertex.property('join_date', self.join_date)
        vertex.property('bio', self.bio)
        vertex.next()