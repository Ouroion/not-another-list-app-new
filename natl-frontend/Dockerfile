FROM node:16

WORKDIR /opt/natl-frontend

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

#COPY src src
#COPY public public

COPY natl-frontend .

CMD ["bash", "-c", "npm run-script start" ]