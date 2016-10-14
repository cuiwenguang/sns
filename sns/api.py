from tastypie.api import Api

from member.resources.auth import AuthResource

v1_api = Api(api_name=u'v1.0')

v1_api.register(AuthResource())
