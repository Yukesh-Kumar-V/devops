writeFile file: 'Dockerfile', text: """
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests
EXPOSE 5000
CMD ["python", "analogclock.py"]
"""
