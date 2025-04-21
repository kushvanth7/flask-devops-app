# Flask DevOps App

This project demonstrates how to build and deploy a simple Flask application using Docker and DevOps practices.

## Features

- Flask-based web application
- Dockerized for consistent environments
- Ready for CI/CD and cloud deployment

## How to Run

```bash
# Build the image
docker build -t flask-devops-app .

# Run the container
docker run -d -p 5000:5000 flask-devops-app
```

Visit `http://localhost:5000` to view the app.