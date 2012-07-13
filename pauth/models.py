from django.db import models
from django.contrib.auth.models import User

class PAuthUser(models.Model):
    user       = models.ForeignKey(User, related_name='pauth_user')
    username   = models.CharField(max_length=512, blank=False)
    provider   = models.CharField(max_length=64, blank=False)
    identifier = models.URLField(max_length=512, blank=False)
    avatar     = models.URLField(max_length=512, blank=True)
    url        = models.URLField(max_length=512, blank=True)

    def __unicode__(self):
        return u"PAuthUser:%s(%s)[User.id:%d]" % (provider, username, user.pk)

class ProviderMetadata(models.Model):
    pauthuser   = models.ForeignKey(PAuthUser, related_name='provider_meta')
    key         = models.CharField(max_length=64, blank=False)
    value       = models.CharField(max_length=512, blank=False)

    def __unicode__(self):
        return u"ProviderMeta(%s) {'%s': '%s'}" % (pauthuser.provider, key, value)
