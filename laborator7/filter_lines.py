def filter_lines(input_file, output_file, keyword):
    fin = open(input_file, "r", encoding="utf-8")
    fout = open(output_file, "w", encoding="utf-8")

    for line in fin:
        if keyword in line:
            fout.write(line)

    fin.close()
    fout.close()


# Exemplu de utilizare
filter_lines("ex3.txt", "filtered.txt", "Python")
print("Fișierul filtered.txt a fost creat.")
