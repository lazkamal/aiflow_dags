FROM alpine:latest

RUN apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main git

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
