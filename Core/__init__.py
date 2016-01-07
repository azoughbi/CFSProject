from django.db.models.signals import post_syncdb
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


def add_view_permissions(sender, **kwargs):
    """
    This syncdb hooks take care of adding view permission to all ContentModel types
    """

    for content_type in ContentType.objects.all():
        codename = "view_%s" % content_type.model

        if not Permission.objects.filter(content_type=content_type, codename=codename):
            # Add the permission
            Permission.objects.create(
                content_type = content_type,
                codename = codename,
                name = "Canview %s" % content_type.name
            )

            print "Added view permission for %s" % content_type.name

post_syncdb.connect(add_view_permissions)