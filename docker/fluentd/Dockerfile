FROM fluent/fluentd:v1.11.2-1.0
USER root
RUN apk update && \
  apk add --no-cache tzdata && \
  cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
  echo "Asia/Tokyo" > /etc/timezone && \
  apk del tzdata
COPY conf/fluentd-custom.conf /fluentd/etc/fluentd-custom.conf
USER fluent
EXPOSE 24224