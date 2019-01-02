FROM python:3.5-slim AS build-env

# You can build the docker image with the command :
# docker build --no-cache -t ing .

# You can create a container with :
# docker run -it --rm -e ING_NUM_CLIENT=$ING_NUM_CLIENT -e ING_DATE_NAISSANCE=$ING_DATE_NAISSANCE -e ING_CODE=$ING_CODE ing

RUN apt-get update \
&& apt-get -y install libglib2.0 \
&& apt-get clean \
&& pip install -U --no-cache-dir --target /app ingdirect \
&& find /app | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

FROM gcr.io/distroless/python3

COPY --from=build-env /app /app
COPY --from=build-env /usr/lib/x86_64-linux-gnu/libgthread-2.0.a /usr/lib/x86_64-linux-gnu/libgthread-2.0.a
COPY --from=build-env /usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0 /usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0
COPY --from=build-env /lib/x86_64-linux-gnu/libglib-2.0.so.0 /lib/x86_64-linux-gnu/libglib-2.0.so.0
COPY --from=build-env /lib/x86_64-linux-gnu/libglib-2.0.so.0.5000.3 /lib/x86_64-linux-gnu/libglib-2.0.so.0.5000.3
COPY --from=build-env /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libpcre.so.3

ENV PYTHONPATH=/app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["python", "/app/bin/ing.py"]