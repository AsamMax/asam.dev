from comfort import comfy


class CookieMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        request.colorMode = int(comfy.firstTrue(
            request.COOKIES.get('colorMode'), 0))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class ConstantsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        request.myMail = "max@asam.dev"

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
