import sys

if len(sys.argv) != 2:
    exit("Error: No File provided")

try:
    file = open(sys.argv[1], "r+")

except:
    exit("Error: Could not open the provided file")

lines = file.readlines()
output = []

for line in lines:
    if line.find("<title>") >= 0:
        title = input("Provide a title: ")
        output.append(f"<title>{title}</title>\n")

    elif line.find("</head>") >= 0:
        output.append("""  <link rel="stylesheet" href="../../assets/css/paper.css">\n""")
        output.append("""  <link rel="icon" href="../../assets/drawable/logo_dark.svg">\n""")
        output.append("""  <script src="../../assets/js/icon_2.js"></script>\n""")
        output.append("""</head>\n""")

    elif line.find("<body") >= 0:
        parent = input("Provide the name of the parent page: ")
        output.append(f"""  <a href="../../{parent}/{parent}.html" id="back"><</a>\n""")
        output.append( """  <div id="background"></div>\n""")

    elif line.find("</body>") >= 0:
        output.append("""  <footer>\n""")
        output.append("""    <a href="../impressum/impressum.html">Impressum</a>\n""")
        output.append("""    <p>© Adam Koprek 2024</p>\n""")
        output.append("""  </footer>\n""")
        output.append("""</body>\n""")

    else:
        output.append(line)

file.seek(0)
file.truncate()
file.writelines(output)
file.close()
