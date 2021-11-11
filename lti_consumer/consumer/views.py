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
These are the views for the LTI consumer.
'''

import sys

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from lti import ToolConsumer

from consumer.forms import TestcaseForm, LaunchParamForm
from consumer.models import Testcase, LaunchParam, DefaultLaunchParam


def index(request):
    '''
    Displays the main page.

    Keyword arguments:
        request -- the calling HttpRequest
    '''
    return render(request, 'consumer/index.html', {})


def create_testcase(request):
    '''
    Displays a form to create a testcase.

    Keyword arguments:
        request -- the calling HttpRequest
    '''
    if request.method == 'POST':
        form = TestcaseForm(request.POST)
        if form.is_valid():
            tc = form.save()
            return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                                args=(tc.id,)))

    else:
        form = TestcaseForm()

    return render(request, 'consumer/create_testcase.html', {'form': form})


def edit_testcase(request, testcase_id):
    '''
    Displays a form to edit a testcase.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase to edit
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    if request.method == 'POST':
        form = TestcaseForm(request.POST, instance=testcase)
        if form.is_valid():
            tc = form.save()
            return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                                args=(tc.id,)))

    else:
        form = TestcaseForm(instance=testcase)

    params = {'form': form, 'testcase': testcase}
    return render(request, 'consumer/edit_testcase.html', params)


def list_testcase(request):
    '''
    Lists all testcases.

    Keyword arguments:
        request -- the calling HttpRequest
    '''
    testcases = Testcase.objects.all().order_by('-published_at')

    return render(request, 'consumer/list_testcase.html',
                  {'testcases': testcases})


def show_testcase(request, testcase_id):
    '''
    shows a testcase with all parameters.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase to show
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)

    lps = {}
    for lp in testcase.launchparam_set.all():
        lps[lp.name] = lp.value

    params = {'testcase': testcase}

    try:
        consumer = ToolConsumer(
            consumer_key=testcase.consumer_key,
            consumer_secret=testcase.consumer_secret,
            launch_url=testcase.launch_url,
            params=lps
        )
        params['launch_data'] = consumer.generate_launch_data()
        params['launch_url'] = consumer.launch_url
    except Exception as inst:
        params['error_name'] = str(type(inst).__name__)
        params['error_detail'] = str(inst)

    return render(request, 'consumer/show_testcase.html', params)


def delete_testcase(request, testcase_id):
    '''
    deletes a testcase.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase to delete
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    testcase.delete()
    return HttpResponseRedirect(reverse('consumer.views.list_testcase'))


def delete_launch_param(request, testcase_id, launch_param_id):
    '''
    deletes a launch parameter.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase with the launch parameter
        lauch_param_id -- id of the launch parameter to delete
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    launch_param = get_object_or_404(LaunchParam, id=launch_param_id)
    launch_param.delete()
    return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                        args=(testcase.id,)))


def edit_launch_param(request, testcase_id, launch_param_id):
    '''
    edits a launch parameter.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase with the launch parameter
        lauch_param_id -- id of the launch parameter to edit
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    launch_param = get_object_or_404(LaunchParam, id=launch_param_id)
    if request.method == 'POST':
        form = LaunchParamForm(request.POST, instance=launch_param)
        if form.is_valid():
            lp = form.save(commit=False)
            lp.testcase = testcase
            lp.save()
            return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                                args=(testcase.id,)))

    else:
        form = LaunchParamForm(instance=launch_param)

    default_launch_params = DefaultLaunchParam.objects.all()
    params = {'form': form, 'testcase': testcase, 'launch_param': launch_param,
              'default_launch_params': default_launch_params}
    return render(request, 'consumer/edit_launch_param.html', params)


def create_launch_param(request, testcase_id):
    '''
    creates a launch parameter.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase with the launch parameter
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    if request.method == 'POST':
        form = LaunchParamForm(request.POST)
        if form.is_valid():
            lp = form.save(commit=False)
            lp.testcase = testcase
            lp.save()
            return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                                args=(testcase.id,)))

    else:
        form = LaunchParamForm()

    default_launch_params = DefaultLaunchParam.objects.all()
    params = {'form': form, 'testcase': testcase,
              'default_launch_params': default_launch_params}
    return render(request, 'consumer/create_launch_param.html', params)


def copy_testcase(request, testcase_id):
    '''
    copy a testcase.

    Keyword arguments:
        request -- the calling HttpRequest
        testcase_id -- id of the testcase to edit
    '''
    testcase = get_object_or_404(Testcase, id=testcase_id)
    new_testcase = Testcase.objects.create(
        name=testcase.name + ' (copy)',
        launch_url=testcase.launch_url,
        consumer_key=testcase.consumer_key,
        consumer_secret=testcase.consumer_secret
    )
    for p in testcase.launchparam_set.all():
        new_testcase.launchparam_set.create(name=p.name, value=p.value)

    return HttpResponseRedirect(reverse('consumer.views.show_testcase',
                                        args=(new_testcase.id,)))
