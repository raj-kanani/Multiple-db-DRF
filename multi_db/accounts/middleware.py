from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization")

    def __call__(self, request):
        print("run before the view ")
        response = self.get_response(request)
        print("run after the view")
        return response

    # @staticmethod
    # def get_current_user(request):
    #     if request.user.is_authenticated:
    #         return request.user
    #     else:
    #         return None
    @staticmethod
    def get_current_user(self):
        # Access user information without relying on request object
        if hasattr(self, 'request') and hasattr(self.request, 'user'):
            return self.request.user
        else:
            return AnonymousUser()

    # def process_view(self, request, view_func, *view_args, **view_kargs):
    #     pass
    #
    # def process_exception(self, request, exception):
    #     pass

# def __init__(self, get_response):
#     self.get_response = get_response
#     print("one time initialization")
#
# def __call__(self, request):
#     print("before view")
#     if request.user.is_authenticated:
#         request.username = request.user.username
#     else:
#         request.username = None
#
#     response = self.get_response(request)
#     print("after view")
#     return response
