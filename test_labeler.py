from django import forms
from form_mapper import LabelMapper
from datetime import date
import pytest


class DogForm(forms.Form, LabelMapper):
    name = forms.CharField(label='Dog name')
    birthday = forms.DateField(required=False)


def test_data_required():
    with pytest.raises(ValueError):
        DogForm.from_data()


def test_basic_inverted_data():
    form = DogForm.from_data({'Dog name': 'Rex'})
    assert form.is_valid()
    assert form.cleaned_data == {
        'name': 'Rex',
        'birthday': None,
    }


def test_more_inverted_data():
    form = DogForm.from_data({'Dog name': 'Rex', 'birthday': date.today()})
    assert form.is_valid()
    assert form.cleaned_data == {
        'name': 'Rex',
        'birthday': date.today(),
    }


def test_invalid_names():
    form = DogForm.from_data({'Dog\'s name': 'Rex', 'Birthday': date.today()})
    assert not form.is_valid()

    form = DogForm.from_data({'Dog name': 'Rex'})
    assert form.is_valid()
    assert form.cleaned_data == {
        'name': 'Rex',
        'birthday': None,
    }


def test_remapping():
    """Should be able to provide alternae mapping"""
    form = DogForm.from_data(
        {'Dog\'s name': 'Rex', 'birthday': date.today()},
        mapping={'name': 'Dog\'s name'},
    )
    assert form.is_valid()
    assert form.cleaned_data == {
        'name': 'Rex',
        'birthday': date.today(),
    }

