==================
Django Form Mapper
==================

A little bitty utility for making it easier to use forms to validate data
pulled from other sources.

Why?
====

Say you have some data that you're importing from an external source, like a
CSV file. You want to validate the data before trying to add it to your database,
maybe to avoid database-related exceptions, maybe to provide useful user
feedback, whatever.

Maybe the shape of the data corresponds to an existing form class or maybe it
occurred to you that, hey, `django.forms` already provides pretty extensive
functionality for validating data pretty extensively, maybe I could make use
of that to validate my CSV (or whatever) data.

Except nobody uses your elegant form field names, the headers are all, like,
human readable. Like labels. So what if you could use the field labels as the
field keys?

This utility mixin provides a classmethod that lets you initialize a form using
your existing data and your form labels as the keys - or whatever alternate
'label' to field name mapping you provide.

Usage
=====

Use the mixin with your form class::

    from form_mapper import LabelMapper

    class MyForm(LabelMapper, forms.Form):
        name = forms.CharField(label="What is your name?")
        

Initialize a new form instance::

    >>> non_form_post_data = {"What is your name?": "Bob Barker"}
    >>> form = MyForm.from_labels(data=non_form_post_data)
    >>> form.is_valid()
    True
    >>> form.cleaned_data['name']
    'Bob Barker'

License
=======

MIT license
