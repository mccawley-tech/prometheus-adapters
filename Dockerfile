FROM python:3.9.7


COPY ./github .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3300

CMD [ "python3", "github-prometheus.py" ]