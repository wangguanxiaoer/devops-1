from django.db import models


# Create your models here.

class SaltHost(models.Model):
    nodename = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=u'主机名称')
    # salt主机存活状态
    alive = models.BooleanField(default=False, verbose_name=u'连通状态')
    # 上次检测时间
    alive_time_last = models.DateTimeField(auto_now=True)
    # 当前检测时间
    alive_time_now = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name=u'是否加入salt管理')

    def __str__(self):
        return self.nodename

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_deploy", u"查看主机部署"),
            ("edit_deploy", u"管理主机部署"),
            ("edit_salthost", u"管理Salt主机"),
        )
        verbose_name = u'Salt主机授权'
        verbose_name_plural = u'Salt主机授权管理'


class SaltGroup(models.Model):
    # 定义分组别名
    nickname = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=u'Salt分组')
    # 分组后groupname不可变
    groupname = models.CharField(
        max_length=80,
        unique=True)
    minions = models.ManyToManyField(
        SaltHost,
        related_name='salt_host_set',
        verbose_name=u'Salt主机')

    def __str__(self):
        return self.nickname

    class Meta:
        default_permissions = ()
        permissions = (
            ("edit_saltgroup", u"管理Salt主机分组"),
        )
        verbose_name = u'Salt分组'
        verbose_name_plural = u'Salt分组管理'
