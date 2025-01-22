# define a class named LfAdmin with two parameters : logical_id and role_arn
class LfAdmin:
    def __init__(self, logical_id, role_arn):
        self.logical_id = logical_id
        self.role_arn = role_arn
