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
This the url configuration for the LTI consumer.
'''

from django.conf.urls import url
from consumer.views import *


urlpatterns = [
    url(r'^$', index, name='consumer.views.index'),
    url(r'^testcase/create$', create_testcase,
        name='consumer.views.create_testcase'),
    url(r'^testcase/(?P<testcase_id>\d+)$', show_testcase,
        name='consumer.views.show_testcase'),
    url(r'^testcase/(?P<testcase_id>\d+)/edit$', edit_testcase,
        name='consumer.views.edit_testcase'),
    url(r'^testcase/(?P<testcase_id>\d+)/delete$', delete_testcase,
        name='consumer.views.delete_testcase'),
    url(r'^testcase/$', list_testcase,
        name='consumer.views.list_testcase'),
    url(r'^testcase/(?P<testcase_id>\d+)/launch/param$', create_launch_param,
        name='consumer.views.create_launch_param'),
    url(r'^testcase/(?P<testcase_id>\d+)/launch/param/(?P<launch_param_id>\d+)/edit$',
        edit_launch_param,
        name='consumer.views.edit_launch_param'),
    url(r'^testcase/(?P<testcase_id>\d+)/launch/param/(?P<launch_param_id>\d+)/delete$',
        delete_launch_param,
        name='consumer.views.delete_launch_param'),
]
