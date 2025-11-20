%default INPUT '/data/answers/in/yahoo.csv'
%default STOP '/workspace/stopwords_es_en.txt'
%default OUTPUT '/data/answers/out/yahoo_wordfreq'

A = LOAD '$INPUT' USING PigStorage('\t') AS (id:chararray, text:chararray);
B = FOREACH A GENERATE id, LOWER(text) AS text;
C = FOREACH B GENERATE id, REPLACE(text, '[^a-z0-9áéíóúñü ]', ' ') AS clean;
D = FOREACH C GENERATE id, FLATTEN(TOKENIZE(clean)) AS word;
E = FILTER D BY (word IS NOT NULL) AND (SIZE(TRIM(word)) > 0) AND NOT (word MATCHES '^[0-9]+$');
SW = LOAD '$STOP' USING PigStorage('\n') AS (stop:chararray);
F = JOIN E BY word LEFT OUTER, SW BY stop;
G = FOREACH F GENERATE E::word AS word, SW::stop AS s;
H = FILTER G BY s IS NULL;
I = GROUP H BY word;
J = FOREACH I GENERATE group AS word, COUNT(H) AS cnt;
K = ORDER J BY cnt DESC;
STORE K INTO '$OUTPUT' USING PigStorage('\t');
