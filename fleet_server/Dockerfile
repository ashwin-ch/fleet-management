# Choose the docker image  which needs to be used as baseline
FROM node:17

# Expose the port for server access port
EXPOSE 4000

# create working directory
WORKDIR /app

COPY . .

# install json-server
RUN npm install -g json-server

# removing the below configuration to enable json-server working in kubernetes
ENTRYPOINT [ "json-server", "--watch", "db.json", "--port", "4000"]