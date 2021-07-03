"""
Managed API images service
For more information, see README.md.
"""

from google.appengine.api import images, app_identity
from google.appengine.ext import ndb
import ujson
import logging
import re

import webapp2

# Constants
service_url = '/images'

# Functions
def camel_to_hyphen(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

def get_filename(path):
    default_bucket = app_identity.get_default_gcs_bucket_name()
    return '/gs/' + default_bucket + path

def get_serving_url(path):
    # return get_filename(path)
    url = images.get_serving_url(
        None,
        secure_url=True,
        filename=get_filename(path)
    )
    return url

def handle_errors(self, func):
    try:
        return func()
    except Exception as e:
        logging.error('Images service error', e);
        code = camel_to_hyphen(e.__class__.__name__)
        status = 400
        if code == 'object-not-found-error':
            status = 404
        error_response(self, status, code, e.message)
    return


def error_response(self, status, code, message):
    self.response.set_status(status)
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(ujson.dumps({
        'error': {
            'code': code,
            'message': message
        }
    }))

def path_required(self):
    error_response(self, 400, 'required', 'The path parameter is required')

def not_found(self):
    error_response(self, 404, 'not-found', 'Resource not found at the path specified')

def not_found_endpoint(self):
    error_response(self, 404, 'not-found', 'Endpoint not found')

# Handlers
class ServingUrlRedirect(webapp2.RequestHandler):
    def get(self):
        def request_handler():
            path = self.request.get('path')
            if path:
                url = get_serving_url(path)
                self.redirect(url)
                return
            path_required(self)
        handle_errors(self, request_handler)
        return

class ServingUrlGenerator(webapp2.RequestHandler):
    def get(self):
        def request_handler():
            path = self.request.get('path')
            if path:
                url = get_serving_url(path)
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.out.write(url)
                return
            path_required(self)
        handle_errors(self, request_handler)
        return


app = webapp2.WSGIApplication([
    (service_url + '/serving-url', ServingUrlGenerator),
    (service_url + '/serving-url/redirect', ServingUrlRedirect),
], debug=True)
# [END all]
