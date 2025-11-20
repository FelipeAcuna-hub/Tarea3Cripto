# guarda como ask_llm.py
import os, csv, time, argparse
from typing import List
from openai import OpenAI

SYSTEM = "Responde de forma breve, objetiva y factual. Si no estás seguro, dilo explícitamente."

def load_questions(path: str) -> List[tuple]:
    rows = []
    with open(path, encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t")
        for row in r:
            if len(row) >= 2:
                rows.append((row[0], row[1]))
    return rows

parser = argparse.ArgumentParser()
parser.add_argument("--questions", default="out/questions.tsv")
parser.add_argument("--model", default="gpt-4o-mini")
parser.add_argument("--rate_delay", type=float, default=0.7, help="delay entre requests (s)")
args = parser.parse_args()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
qs = load_questions(args.questions)

os.makedirs("out", exist_ok=True)
with open("out/llm.csv","w",encoding="utf-8",newline="") as fo:
    w = csv.writer(fo, delimiter="\t")
    for qid, qtext in qs:
        try:
            resp = client.chat.completions.create(
                model=args.model,
                messages=[
                    {"role":"system","content": SYSTEM},
                    {"role":"user","content": qtext}
                ],
                temperature=0.2,
                max_tokens=256,
            )
            ans = resp.choices[0].message.content.strip()
        except Exception as e:
            ans = f"[ERROR] {e}"
        w.writerow([qid, ans])
        time.sleep(args.rate_delay)

print("OK -> out/llm.csv")
