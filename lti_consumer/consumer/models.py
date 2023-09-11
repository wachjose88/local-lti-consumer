# Copyright (c) 2018 Josef Wachtler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
These are the database models for the LTI consumer.
'''
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class DefaultLaunchParam(models.Model):
    '''
    This model stores names of launch parameters which are allowed.
    Entries for this model are created automatically on db init.

    Fields
        name -- the name of the launch parameter
        required -- true if this parameter is required for a valid LTI launch.
    '''
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    required = models.BooleanField(verbose_name=_('Required'))

    def __str__(self):
        '''
        unicode representation
        '''
        return self.name

    class Meta:
        verbose_name = _('Default Launch Parameter')
        verbose_name_plural = _('Default Launch Parameters')


class Testcase(models.Model):
    '''
    This model stores a testcase.

    Fields
        name -- the name of the testcase
        launch_url -- url of the LTI provider to test
        consumer_key -- the consumer key of the LTI provider
        consumer_secret -- the consumer secret of the LTI provider
        published_at -- time of creating the Testcase
    '''
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    launch_url = models.URLField(verbose_name=_('Launch URL'))
    consumer_key = models.CharField(max_length=200,
                                    blank=True,
                                    verbose_name=_('Consumer key'))
    consumer_secret = models.CharField(max_length=200,
                                       blank=True,
                                       verbose_name=_('Consumer secret'))
    published_at = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Published at'))

    def __str__(self):
        '''
        unicode representation
        '''
        return self.name

    class Meta:
        verbose_name = _('Testcase')
        verbose_name_plural = _('Testcases')


class LaunchParam(models.Model):
    '''
    This model stores the launch parameters of a testcase.

    Fields
        testcase -- the corresponding testcase
        name -- the name of the launch parameter
        value -- the value for the named launch parameter
    '''
    testcase = models.ForeignKey(Testcase,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Testcase'))
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    value = models.CharField(max_length=200, blank=True,
                             verbose_name=_('Value'))

    def __str__(self):
        '''
        unicode representation
        '''
        return self.name

    class Meta:
        verbose_name = _('Launch Parameter')
        verbose_name_plural = _('Launch Parameters')
