import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("ruble", "1")
text1=html.escape(text1)
text2 = form.getfirst("kurs", "1")
text2=html.escape(text2)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>Конвертер рублей в доллары </title>
        </head>
        <body>""")

print("<h1>Конвертер</h1>")
print("<p>Курс доллара: {} </p>" .format(text1))
print("<p>Доллары: {} </p>" .format(text2))

print("""</body>
        </html>""")
