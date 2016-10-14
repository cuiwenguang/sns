import json

class Rest:
    @classmethod
    def result(cls, data, status=200, msg='', ser=False):
        r = {
            "satus": status,
            "msg": msg,
            "data": data
        }
        if ser:
            return json.dumps(r)

        return r

        SUCCESS = 200
        NO_CONTENT = 204
        PARAM_INVALID = 405
        VALIDATE_ERROR = 450
        ERROR = 500