import arrow

from django.conf import settings


def get_current_server_time_info():
    timezone = settings.TIME_ZONE
    current_time_info = arrow.utcnow()

    return {'timezone': timezone, 'timestamp': int(current_time_info.format('x')) // 1000, 'formatted_datetime': current_time_info.to(timezone).format('YYYY-MM-DD HH:mm:ss ZZ')}


def get_local_time_info(timestamp: int, timezone: str):
    time_info = arrow.get(timestamp // 1000, tzinfo='UTC').to(timezone).format('YYYY-MM-DD HH:mm:ss ZZ')

    return {'timezone': timezone, 'timestamp': timestamp, 'formatted_datetime': time_info}
