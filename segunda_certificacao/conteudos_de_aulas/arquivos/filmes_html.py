filmes = {
    "drama": ["A Procura da Felicidade", "Joker"],
    "comédia": ["Os Farofeiros", "Se Beber Não Case"],
    "Ação": ["Velozes e Furiosos", "Missão Impossível"],
    "Fantasia": ["Harry Potter", "Castelo Ratimbum"]
}
with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
        <html>
        <head>
            <title>Filmes</title>
        </head>
        <body>
    """)
    for genero, nomes in filmes.items():
        pagina.write(f"<h1>{genero}</h1>")
        for filme in nomes:
            pagina.write(f"<p>{filme}</p>")
    pagina.write("</body></html>")
