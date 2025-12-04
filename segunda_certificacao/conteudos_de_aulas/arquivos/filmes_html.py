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
    <body>""")
    for genero, nomes in filmes.items():
        pagina.write(f"\n\t\t<h1>{genero}</h1>\n") # o caractere especial '\t' ajusta a tabulação (identação)
        pagina.write(f"\t\t<ul>\n") # o caractere especial '\n' quebra a linha
        for filme in nomes:
            pagina.write(f"\t\t\t<li>{filme}</li>\n")
        pagina.write(f"\t\t</ul>\n")
    pagina.write("\t</body>\n\t</html>")
