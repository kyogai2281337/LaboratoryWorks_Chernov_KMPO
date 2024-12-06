FROM mysql:latest

LABEL author=nemesidaa

RUN chown -R mysql:root /var/lib/mysql/

ARG MYSQL_DATABASE=book_shop
ARG MYSQL_USER=nemesidaa
ARG MYSQL_PASSWORD=passwd
ARG MYSQL_ROOT_PASSWORD=root

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

ADD db.sql /etc/mysql/data.sql

RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /etc/mysql/data.sql
RUN cp /etc/mysql/data.sql /docker-entrypoint-initdb.d
EXPOSE 3306

