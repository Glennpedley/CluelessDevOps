FROM python:3.9-slim
COPY . /CluelessDevOps
WORKDIR /CluelessDevOps
RUN pip install --target=/whatsapp-actions twilio
RUN chmod +x /CluelessDevOps/main.py
CMD ["python3.9", "/CluelessDevOps/main.py"]
