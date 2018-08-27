FROM redis
WORKDIR /data
COPY redis.conf /data/
EXPOSE 6379
CMD ["redis-server","/data/redis.conf"]
