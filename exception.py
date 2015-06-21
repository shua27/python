from threading import thread


try:
    print(100/0)
except Exception as e:
    print(str(e))


