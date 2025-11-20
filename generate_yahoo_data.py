import csv, os, random

os.makedirs("out", exist_ok=True)

# Preguntas variadas estilo Yahoo Respuestas
questions = [
    "¿Cómo puedo mejorar mi rendimiento académico?",
    "Mi gato no quiere comer, ¿qué puedo hacer?",
    "¿Cuál es la capital de Francia?",
    "¿Qué beneficios tiene correr todos los días?",
    "¿Cómo elimino virus de mi computador?",
    "¿Qué diferencia hay entre IPv4 e IPv6?",
    "¿Cómo puedo ahorrar dinero siendo estudiante?",
    "¿Cuál es la mejor manera de aprender Python?",
    "¿Qué pasa si dejo mi celular cargando toda la noche?",
    "¿Por qué el cielo es azul?",
    "¿Cómo puedo bajar de peso saludablemente?",
    "¿Cuáles son los efectos del cambio climático?",
    "¿Qué tan seguro es comprar por Internet?",
    "¿Cuál es la función de la memoria RAM?",
    "¿Qué significa soñar con agua?",
]

# Respuestas estilo Yahoo (más informales)
answers_yahoo = [
    "Estudia con tiempo y no dejes todo para el último día, eso me funcionó.",
    "Llévalo al veterinario, puede tener algo en el estómago.",
    "París, obviamente.",
    "Ayuda con la salud y te da más energía, aunque también depende de la dieta.",
    "Usa un antivirus gratis como Avast o Malwarebytes.",
    "IPv4 usa 32 bits, IPv6 usa 128 bits, y hay más direcciones.",
    "Haz un presupuesto y evita comprar cosas innecesarias.",
    "Busca tutoriales en YouTube, yo aprendí así.",
    "No pasa nada grave, solo gasta más electricidad.",
    "Por la dispersión de la luz solar en la atmósfera.",
    "Haz ejercicio y come menos pan o comida chatarra.",
    "Provoca calor, sequías y afecta a los animales.",
    "Depende del sitio, revisa que tenga buenas reseñas.",
    "Guarda los datos que usa tu PC en ese momento.",
    "Dicen que el agua representa emociones o limpieza interior.",
]

# Guardar preguntas
with open("out/questions.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    for i, q in enumerate(questions, start=1):
        w.writerow([i, q])

# Guardar respuestas Yahoo
with open("out/yahoo.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    for i, a in enumerate(answers_yahoo, start=1):
        w.writerow([i, a])

print("✅ Generado: out/questions.tsv y out/yahoo.csv (", len(questions), "preguntas )")
