FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8

USER root

# Descarga directa de Pig 0.17 (usamos el archivo de archivo oficial estable)
ADD https://archive.apache.org/dist/pig/pig-0.17.0/pig-0.17.0.tar.gz /tmp/pig.tgz

RUN mkdir -p /opt \
 && tar -xzf /tmp/pig.tgz -C /opt \
 && ln -s /opt/pig-0.17.0 /opt/pig \
 && rm -f /tmp/pig.tgz

ENV PIG_HOME=/opt/pig
ENV PATH=$PIG_HOME/bin:$PATH

# Mantén el contenedor vivo
CMD ["bash","-lc","sleep infinity"]
