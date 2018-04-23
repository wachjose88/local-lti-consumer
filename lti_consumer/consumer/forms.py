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
These are the forms for the LTI consumer.
'''

from django.forms import ModelForm

from consumer.models import Testcase, LaunchParam


class TestcaseForm(ModelForm):
    '''
    This form is used to create and to edit a testcase for a LTI prvider.
    '''
    class Meta:
        model = Testcase
        fields = ['name', 'launch_url', 'consumer_key', 'consumer_secret']

    def __init__(self, *args, **kwargs):
        '''
        The constructor adds some attributes to the HTML widgets.
        '''
        super(TestcaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['aria-describedby'] = visible.html_name


class LaunchParamForm(ModelForm):
    '''
    This form adds some launch parameters to a testcase.
    '''
    class Meta:
        model = LaunchParam
        fields = ['name', 'value']

    def __init__(self, *args, **kwargs):
        '''
        The constructor adds some attributes to the HTML widgets and sets the
        names from the default launch parameters as a list to the name field.
        '''
        super(LaunchParamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['aria-describedby'] = visible.html_name
            self.fields['name'].widget.attrs['list'] = 'default_launch_params'
