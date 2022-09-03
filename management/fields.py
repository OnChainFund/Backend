from django.db.models import DurationField
from django.utils.duration import _get_duration_components


class CustomDurationField(DurationField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val is None:
            return ""

        days, hours, minutes, seconds, microseconds = _get_duration_components(val)
        return "{} days, {:02d} hours, {:02d} minutes, {:02d}.{:06d} seconds".format(
            days, hours, minutes, seconds, microseconds
        )
