"""
Django form class mixin that eases data ingestion and validation using
alternative keys for field names.
"""

# TODO handle translated strings

class LabelMapper(object):

    @classmethod
    def from_data(cls, data=None, language=None, mapping=None, *args, **kwargs):
        """
        Initialize a form instance using data with alternate keys

        Args:
            data: submitted form data using labels as keys
            language: language code
            mapping: dictionary with different label mapping
            *args: form *args
            **kwargs: form **kwargs

        Returns:
            An instance of the associated form class

        """

        if data is None:
            raise ValueError('Must provide data')

        mapping = {} if mapping is None else mapping

        starting_mapping = {
            field_name: field.label or field_name
            for field_name, field in cls.base_fields.items()
        }
        starting_mapping.update(mapping)

        field_labels = {
            v: k for k, v in starting_mapping.items()
        }

        updated_data = {
            field_labels[key]: value
            for key, value in data.items()
            if key in field_labels
        }

        kwargs.update({'data': updated_data})

        return cls(*args, **kwargs)
