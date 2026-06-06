FROM python:3.13-slim

# Non-interactive matplotlib + reproducible threading defaults
ENV MPLBACKEND=Agg \
    OMP_NUM_THREADS=4 \
    PYTHONHASHSEED=0 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspace

EXPOSE 8888 8080

CMD ["python"]
