import falcon
import re
import requests


class ApiResource:
    def on_get(self, req, resp):
        """Handles GitHub get requests"""

        payload = {
            u'client_id': u'3b2242bbaa9ba869d0c3',
            u'client_secret': u'dbee0e77721d3552d7c9950bdf312398b65b6852',
            u'code': req.get_param(u'code', required=True)
        }
        response = requests.post(u'https://github.com/login/oauth/access_token', data=payload)

        p = re.compile(ur'^access_token=(.*?)&.*$')
        token = re.search(p, response.text)

        resp.body = "Your accesstoken is %s" % token.groups()

app = falcon.API()
app.add_route('/', ApiResource())
