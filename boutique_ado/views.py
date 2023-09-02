from django.views.defaults import (
    permission_denied,
    bad_request,
    page_not_found,
    server_error,
)


def custom_bad_request_view(
    request, exception, template_name="errors/400.html"
):
    """Override the default bad request view to display custom 400 page
    on specific URL path"""
    return bad_request(request, exception, template_name)


def custom_permission_denied_view(
    request, exception, template_name="errors/403.html"
):
    """Override the default permission denied view to display custom 403 page
    on specific URL path"""
    return permission_denied(request, exception, template_name)


def custom_page_not_found_view(
    request, exception, template_name="errors/404.html"
):
    """Override the default page not found view to display custom 404 page
    on specific URL path"""
    return page_not_found(request, exception, template_name)


def custom_server_error_view(request, template_name="errors/500.html"):
    """Override the default server error view to display custom 500 page
    on specific URL path"""
    return server_error(request, template_name)
