# guarda como get_yahoo_sample.py
import csv, os, re, random, argparse, pandas as pd

def clean_text(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = re.sub(r"<[^>]+>", " ", s)        # quita HTML
    s = s.replace("\r"," ").replace("\n"," ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

parser = argparse.ArgumentParser()
parser.add_argument("--src", required=True, help="Ruta al CSV de Yahoo (Kaggle/Webscope exportado a CSV)")
parser.add_argument("--qcol", default="question_content", help="columna de la pregunta")
parser.add_argument("--acol", default="best_answer", help="columna de la respuesta (mejor o principal)")
parser.add_argument("--n", type=int, default=200, help="muestras")
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

random.seed(args.seed)
df = pd.read_csv(args.src)
# filtra filas válidas
df = df[[args.qcol, args.acol]].dropna()
df[args.qcol] = df[args.qcol].map(clean_text)
df[args.acol] = df[args.acol].map(clean_text)
df = df[(df[args.qcol].str.len()>0) & (df[args.acol].str.len()>0)]

# sample reproducible
if len(df) > args.n:
    df = df.sample(n=args.n, random_state=args.seed).reset_index(drop=True)

os.makedirs("out", exist_ok=True)
# guarda preguntas
with open("out/questions.tsv","w",encoding="utf-8",newline="") as fq:
    wq = csv.writer(fq, delimiter="\t")
    for i,(q,a) in enumerate(zip(df[args.qcol], df[args.acol]), start=1):
        wq.writerow([i, q])

# guarda respuestas Yahoo (solo texto respuesta)
with open("out/yahoo.csv","w",encoding="utf-8",newline="") as fy:
    wy = csv.writer(fy, delimiter="\t")
    for i,a in enumerate(df[args.acol], start=1):
        wy.writerow([i, a])

print("OK -> out/questions.tsv y out/yahoo.csv")
