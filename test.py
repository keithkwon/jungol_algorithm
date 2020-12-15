from datetime import datetime

now = datetime.now()
a = 0
a = now.year - 1900 # p
a += now.month - 1  # q
a += now.day

