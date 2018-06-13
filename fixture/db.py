import pymysql


class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host, name, user, password)


    def destroy(self):
        self.connection.close()