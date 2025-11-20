#Tarea 3 Sistemas Distruibuidos 

Para iniciar los contenedores: 
- pig
- nodemanager
- historyserver
- resourceman
- datanode
- namenode 

Se debe realizar por la terminal o por el vs code en el caso donde se vaya ejecutar por ahí, se realiza la ruta a la carpeta de "Tarea3distri" se debe hacer 

#para poder iniciar los contenedores
docker compose up -d 
docker compose ps 
#si esta todo correctamente debería quedar todo en estado UP

#Para cargar los datos al HDFS
Se debe cargar con:

docker compose exec namenode bash -lc "/opt/hadoop-3.2.1/bin/hdfs dfs -mkdir -p /data/answers/in"
docker compose exec namenode bash -lc "/opt/hadoop-3.2.1/bin/hdfs dfs -put -f /workspace/out/yahoo.csv /data/answers/in/yahoo.csv"
docker compose exec namenode bash -lc "/opt/hadoop-3.2.1/bin/hdfs dfs -put -f /workspace/out/llm.csv   /data/answers/in/llm.csv"

#Lo mismo para subir los Stopwords, se realiza con los siguentes comandos

docker compose exec namenode bash -lc "/opt/hadoop-3.2.1/bin/hdfs dfs -mkdir -p /data/answers/aux"
docker compose exec namenode bash -lc "/opt/hadoop-3.2.1/bin/hdfs dfs -put -f /workspace/stopwords_es_en.txt /data/answers/aux/stopwords_es_en.txt"

#Para realizar la ejecución de Apache Pig tuvimos unos problemas para hacerlo con contenedor aparte asi que lo realizamos dentro del contenedor NameNode

docker compose exec namenode bash -lc \
'PIG_OPTS="-Dfs.defaultFS=hdfs://namenode:8020" \
/opt/pig/bin/pig -x mapreduce \
-f /workspace/wordcount_clean.pig \
-param_file /workspace/params_yahoo.properties'

#Para la LLM se realiza el siguente comando 

docker compose exec namenode bash -lc \
'PIG_OPTS="-Dfs.defaultFS=hdfs://namenode:8020" \
/opt/pig/bin/pig -x mapreduce \
-f /workspace/wordcount_clean.pig \
-param_file /workspace/params_llm.properties'

#Para ver que esta bien Pig genera las siguientes salidas

/data/answers/out/yahoo_wordfreq
/data/answers/out/llm_wordfreq

#Para la exportación de resultaods de HDFS
se realiza el siguiente comando 

docker compose exec namenode bash -lc \
"/opt/hadoop-3.2.1/bin/hdfs dfs -cat /data/answers/out/yahoo_wordfreq/part* > /workspace/yahoo_top.tsv"

docker compose exec namenode bash -lc \
"/opt/hadoop-3.2.1/bin/hdfs dfs -cat /data/answers/out/llm_wordfreq/part* > /workspace/llm_top.tsv"

#Para la generación de gráficos comparativos que estan en el informe pero si se quieren realizar se hace 

python topN_compare.py 50

Con eso debería estar funcionando al 100% el laboratorio


