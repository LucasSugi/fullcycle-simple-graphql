from datetime import date
from api.db import FAKE_DB

def createPost_resolver(obj, info, title, description):
    try:
        today = date.today()
        _id = str(len(FAKE_DB)+1).zfill(4)
        FAKE_DB.append({"id": _id, "title":title, "description": description, "created_at": today})
        payload = {
            "success": True,
            "post": FAKE_DB[-1]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": str(error)
        }
    return payload

def updatePost_resolver(obj, info, **kwargs):
    try:
        _id = kwargs.pop("id")
        row = [(index, row) for index, row in enumerate(FAKE_DB) if row.get("id") == _id]
        index = row[0][0]
        post = row[0][1]
        post = {**post, **kwargs}
        FAKE_DB[index] = post
        payload = {
            "success": True,
            "post": FAKE_DB[index]
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

def deletePost_resolver(obj, info, id):
    try:
        post = [row for row in FAKE_DB if row.get("id") == id][0]
        FAKE_DB[:] = [row for row in FAKE_DB if row.get("id") != id]
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
