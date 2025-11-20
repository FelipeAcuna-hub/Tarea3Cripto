#!/usr/bin/env bash
set -euo pipefail
pig -x mapreduce -Dfs.defaultFS=hdfs://namenode:8020 /workspace/wordcount_clean.pig \
  INPUT=/data/answers/in/llm.csv \
  STOP=/workspace/stopwords_es_en.txt \
  OUTPUT=/data/answers/out/llm_wordfreq
