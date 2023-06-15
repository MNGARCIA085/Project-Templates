# Imagen base
FROM node:14-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package.json .
COPY package-lock.json .

# Instalar dependencias
RUN npm ci --only=production

# Copiar el código fuente del cliente
COPY . .

# Construir la aplicación de React
RUN npm run build

# Exponer el puerto del cliente
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
