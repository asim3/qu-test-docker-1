release: cd test_k8s_1 && python3 manage.py migrate
web: gunicorn --chdir test_k8s_1 --workers 3 test_k8s_1.wsgi
