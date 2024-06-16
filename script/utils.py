from datetime import datetime


def convert_to_datetime(date_str, date_format="%Y-%m-%d %H:%M:%S.%f"):
    if not date_str:
        return date_str
    if isinstance(date_str, float):
        return None
    if date_str == 'nan':
        return None
    return datetime.strptime(date_str, date_format)


def strfloat_to_int(value):
    try:
        if value == "nan":
            return None
        return int(float(value))
    except:
        return None
