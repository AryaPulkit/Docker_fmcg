FROM python:3


RUN mkdir -p src
RUN mkdir -p src/templates
WORKDIR /src
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
ADD app.py . 
ADD model.pkl .
ADD request.py .
COPY index.html /src/templates/index.html
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
