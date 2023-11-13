from django.db.models import QuerySet


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def django_filter_warning(get_queryset_func):
    """
    Used to fix a warning in django-filter.
    Ref: https://github.com/carltongibson/django-filter/issues/966
    """

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return QuerySet()
        return get_queryset_func(self)

    return get_queryset
