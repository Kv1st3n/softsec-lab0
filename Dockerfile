FROM python:3.14.6
WORKDIR /the/workdir/path

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

RUN useradd -m app && chown -R app:app /the/workdir/path
USER app

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.api:app"]