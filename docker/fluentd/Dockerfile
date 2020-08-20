FROM fluent/fluentd:v1.11.2-1.0
USER root
RUN apk add --no-cache --update --virtual tzdata \
 && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
 && echo "Asia/Tokyo" > /etc/timezone \
 && apk del tzdata \
 && gem install fluent-plugin-concat \
 && gem install fluent-plugin-cloudwatch-logs \
 && gem sources --clear-all \
 && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

USER fluent
