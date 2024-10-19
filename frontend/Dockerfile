# Node Image
From node:16

# Working Directory
WORKDIR /usr/src/app

# Copy package
COPY package.json ./

# Install dependencies
RUN npm install

# Copy remaining project files
COPY . . 

# Expose port
EXPOSE 3000

# start 
CMD ["npm", "start"]
