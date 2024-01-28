from api.db import FAKE_DB

def listPosts_resolver(obj, info):
    try:
        payload = {
            "success": True,
            "posts": FAKE_DB
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": str(error)
        }
    return payload

def getPost_resolver(obj, info, id):
    try:
        post = [row for row in FAKE_DB if row.get("id") == id][0]
        payload = {
            "success": True,
            "post": post
        }
    except IndexError:
        payload = {
            "success": False,
            "errors": "O id `{}` não existe!".format(id)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": str(error)
        }
    return payload
