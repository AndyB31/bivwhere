FROM python:3.8.13

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 \
  libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
  libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \
  libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 \
  libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 \
  libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates \
  fonts-liberation libnss3 lsb-release xdg-utils wget

WORKDIR /back_end

COPY back_end/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pyppeteer-install

COPY back_end .

ENTRYPOINT ["gunicorn", "--log-level", "INFO", "-b", ":7511", "-t", "120", "run:APP"]