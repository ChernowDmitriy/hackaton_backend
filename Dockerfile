FROM python:3.11.4-slim-bullseye as dev

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app/src

# Copying and installing requirements
COPY requirements.txt /app/src/
RUN pip install -r requirements.txt

# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying actuall application
COPY . /app/src/

CMD ["/usr/local/bin/python", "-m", "core"]
