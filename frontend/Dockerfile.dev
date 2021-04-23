FROM node:15.12.0-alpine3.12

WORKDIR /app/frontend
COPY package.json /app/frontend

ENV REACT_APP_API_BASE_URL=$REACT_APP_API_BASE_URL

EXPOSE 3000
CMD "npm install --legacy-peer-deps && npm start"
