#!/usr/bin/env bash
set -euo pipefail
HDFS_DIR=/data/answers
hdfs dfs -mkdir -p ${HDFS_DIR}/in
hdfs dfs -put -f ./out/yahoo.csv ${HDFS_DIR}/in/yahoo.csv
hdfs dfs -put -f ./out/llm.csv ${HDFS_DIR}/in/llm.csv
echo "Datos cargados a HDFS en ${HDFS_DIR}/in/"
