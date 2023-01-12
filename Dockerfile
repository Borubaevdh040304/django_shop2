FROM ubuntu 

WORKDIR / 

COPY . .

RUN apt-get update 
RUN apt-get install -y apt-utils
RUN apt-get install -y python3-pip 
RUN pip install --upgrade pip
RUN pip install wheel gunicorn
RUN pip install -r req.txt

ENV SECRET_KEY=%*lo6nqatjg123qf5yy!+f05@4a%^of0ob6cuc3cc+zt#q1#wu
ENV DB_NAME=railway
ENV DB_USER=postgres
ENV DB_PASSWORD=yjdWrmvgdM4snAwYLcxT
ENV DB_HOST=containers-us-west-27.railway.app
ENV DB_PORT=5442
ENV DEBUG=1
ENV ALLOWED_HOST=127.0.0.1,djangoshop2-production.up.railway.app
ENV PORT=8000

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi:application



 