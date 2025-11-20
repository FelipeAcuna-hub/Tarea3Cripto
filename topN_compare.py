import sys
import pandas as pd
import matplotlib.pyplot as plt

TOPN = int(sys.argv[1]) if len(sys.argv) > 1 else 50

# Lee TSVs
yahoo = pd.read_csv("yahoo_top.tsv", sep="\t", names=["word", "cnt"], dtype=str, keep_default_na=False)
llm   = pd.read_csv("llm_top.tsv",   sep="\t", names=["word", "cnt"], dtype=str, keep_default_na=False)

# Limpieza básica
yahoo["word"] = yahoo["word"].str.strip()
llm["word"]   = llm["word"].str.strip()

# Convierte cnt a numérico
yahoo["cnt"] = pd.to_numeric(yahoo["cnt"], errors="coerce").fillna(0).astype(int)
llm["cnt"]   = pd.to_numeric(llm["cnt"],   errors="coerce").fillna(0).astype(int)

# Top-N por conjunto
yahoo_top = yahoo.nlargest(TOPN, "cnt").copy()
llm_top   = llm.nlargest(TOPN, "cnt").copy()

# --- Gráfico Yahoo ---
plt.figure()
plt.barh(yahoo_top["word"][::-1], yahoo_top["cnt"][::-1])
plt.title(f"Top {TOPN} palabras - Yahoo!")
plt.tight_layout()
plt.savefig(f"top{TOPN}_yahoo.png", dpi=180)

# --- Gráfico LLM ---
plt.figure()
plt.barh(llm_top["word"][::-1], llm_top["cnt"][::-1])
plt.title(f"Top {TOPN} palabras - LLM")
plt.tight_layout()
plt.savefig(f"top{TOPN}_llm.png", dpi=180)

# Comparación (outer join para ver diferencias; rellena con 0)
merge = pd.merge(
    yahoo_top.rename(columns={"cnt": "cnt_yahoo"}),
    llm_top.rename(columns={"cnt": "cnt_llm"}),
    on="word",
    how="outer"
).fillna(0)

# Asegura numérico tras el fillna
merge["cnt_yahoo"] = merge["cnt_yahoo"].astype(int)
merge["cnt_llm"]   = merge["cnt_llm"].astype(int)

# Si hay muchas filas, muestra las 20 con mayor suma
if not merge.empty:
    merge["_sum"] = merge["cnt_yahoo"] + merge["cnt_llm"]
    merge = merge.sort_values("_sum", ascending=False).head(min(20, len(merge)))
    merge = merge.drop(columns=["_sum"])

    plt.figure()
    ax = merge.plot(x="word", y=["cnt_yahoo","cnt_llm"], kind="bar")
    plt.title("Frecuencia comparada (palabras comunes y distintas)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("comparacion_comunes.png", dpi=180)
else:
    print("[INFO] merge vacío: no hubo términos en común ni distintos dentro del TopN.")
