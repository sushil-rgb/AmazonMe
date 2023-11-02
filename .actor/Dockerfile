FROM cypress/browsers:latest
RUN apt-get update && apt-get install -y python3
RUN echo $(python3 -m site --user-base)
COPY requirements.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update && apt-get install -y python3-pip && pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
