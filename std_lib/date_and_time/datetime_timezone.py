#! /usr/bin/env python3

import datetime

min6 = datetime.timezone(datetime.timedelta(hours=6))
plus6 = datetime.timezone(datetime.timedelta(hours=6))
d_now = datetime.datetime.now(min6)

print(min6, ':', d_now)
print(datetime.timezone.utc, ':', d_now.astimezone(datetime.timezone.utc))

# reformation in current system
d_system = d_now.astimezone()
print(d_system.tzinfo, '   -> ', d_system)