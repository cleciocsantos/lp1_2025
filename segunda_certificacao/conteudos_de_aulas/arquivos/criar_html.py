with open("ds102.html", "w") as arqhtml:
    arqhtml.write("""
    <html>
        <head>
            <title>DS102</title>
        </head>
        <body>
            <h1>Olá, DS102!</h1>
            <p>LP1 fechado com ICC!</p>
    """)
    for linha in range(10):
        arqhtml.write(f"<p>Linha: {linha}</p>")
    arqhtml.write("""
        </body>
    </html>
    """)