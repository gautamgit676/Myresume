from django.core.cache import cache
from django.http import HttpResponse


class RateLimitMiddleware:
    USER_RATE = 50       # Logged-in users
    ANON_RATE = 25       # Anonymous users
    PERIOD = 3600        # 1 hour

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            key = f"user_rate_limit:{request.user.id}"
            rate = self.USER_RATE
        else:
            ip = self.get_client_ip(request)
            key = f"ip_rate_limit:{ip}"
            rate = self.ANON_RATE

        count = cache.get(key)

        if count is None:
            cache.set(key, 1, timeout=self.PERIOD)

        elif count >= rate:
            return HttpResponse(
                "Too Many Requests. Please try again after one hour.",
                status=429,
            )

        else:
            cache.incr(key)

        return self.get_response(request)

    def get_client_ip(self, request):
        forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")