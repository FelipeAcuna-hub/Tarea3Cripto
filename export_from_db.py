import os, csv, psycopg2

dsn = os.environ.get("PG_DSN", "dbname=project user=postgres password=postgres host=localhost port=5432")
os.makedirs("out", exist_ok=True)

conn = psycopg2.connect(dsn)
cur = conn.cursor()

for src in ("yahoo","llm"):
    cur.execute("SELECT id, text FROM answers WHERE source=%s AND text IS NOT NULL", (src,))
    rows = cur.fetchall()
    with open(f"out/{src}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t")
        for r in rows:
            w.writerow([r[0], r[1]])

cur.close(); conn.close()
print("Archivos exportados en ./out/")
