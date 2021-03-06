FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install -g npm@7.6.1 && npm install eslint --save-dev

EXPOSE 3000
CMD "npm update && npm start"