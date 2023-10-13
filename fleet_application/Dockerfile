# Choose the docker image  which needs to be used as baseline
FROM node:17

EXPOSE 3000
EXPOSE 4000


# create working directory
WORKDIR /app


# install dependencies
# RUN npm install
# RUN npx create-react-app fleet-management-app

COPY . .


RUN npm install -g json-server

RUN npm install

