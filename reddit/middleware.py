
class RequestUserMiddleware:
    def process_request(self, request):
        try:
            request.user = request.user
        except:
            request.user = 'AnonymousUser'
