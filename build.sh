set -o errexit

pip install -r requirements.txt

python portfolio/manage.py collectstatic --no-input
