from models.author import AuthorModel

def authenticate (authorname):
    auth = AuthorModel.find_by_authorname(authorname)
    return auth

def identity(payload):
    auth_id = payload['identity']
    return AuthorModel.find_by_authorid(auth_id)