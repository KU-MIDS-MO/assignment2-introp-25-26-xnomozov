def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1

    elif seconds == 0:
        return {}

    time_dict = {}
    hours = seconds // 3600

    if hours > 0:
        time_dict[3600] = hours

    minutes = (seconds - hours * 3600) // 60
    if minutes > 0:
        time_dict[60] = minutes

    sec = (seconds - hours * 3600 - minutes * 60)
    if sec > 0:
        time_dict[1] = sec

    return time_dict


print(breakdown_time(3700))

