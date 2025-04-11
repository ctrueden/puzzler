def fancy_time(se):
    mi = se / 60
    ho = mi / 60
    da = ho / 24
    we = da / 7
    ye = da / 365
    mo = ye * 12
    fmt = lambda n: f"{float(n):.3f}".rstrip('0').rstrip('.')
    message = f"{fmt(se)} seconds"
    if mi >= 1: message += f" / {fmt(mi)} minutes"
    if ho >= 1: message += f" / {fmt(ho)} hours"
    if da >= 1: message += f" / {fmt(da)} days"
    if we >= 1: message += f" / {fmt(we)} weeks"
    if mo >= 1: message += f" / {fmt(mo)} months"
    if ye >= 1: message += f" / {fmt(ye)} years"
    return message
