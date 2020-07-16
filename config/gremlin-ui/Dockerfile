FROM nginx:latest AS builder

RUN apt-get update
RUN apt-get -y install unzip

WORKDIR /temp/

ADD https://github.com/bricaud/graphexp/archive/master.zip master.zip
RUN unzip master.zip

RUN sed 's/const HOST = "localhost"/const HOST = self.location.hostname/' graphexp-master/scripts/graphConf.js > graphConf.js
RUN mv graphConf.js graphexp-master/scripts

FROM nginx:latest

COPY --from=builder /temp/graphexp-master/ /usr/share/nginx/html/

WORKDIR /usr/share/nginx/html