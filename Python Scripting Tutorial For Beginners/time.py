import time

print(time.time())
# 1664136308.5399587 --> total seconds passed since 1970-01-01 00:00:00 UTC

print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=9, tm_mday=26, tm_hour=2, tm_min=5, tm_sec=56, tm_wday=0, tm_yday=269, tm_isdst=0)

localtime = time.localtime()
print(localtime.tm_year) # 2022

print(time.ctime(time.time()))
# Mon Sep 26 02:07:19 2022

