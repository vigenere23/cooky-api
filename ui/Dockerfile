FROM node:14-alpine


WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

EXPOSE 8080

ENTRYPOINT []
CMD yarn serve
