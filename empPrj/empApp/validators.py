from django.core.exceptions import ValidationError

def validate_edu_email(value):
    if not ".edu" in value:
        raise ValidationError('Please Enter Your Educational Email')
    else:
        return value
