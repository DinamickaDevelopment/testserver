import multiprocessing

#bind = "127.0.0.1:8000"
bind = "unix:/tmp/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1