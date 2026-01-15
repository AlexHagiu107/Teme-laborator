def reverse_lines(input_file, output_file):
    fin = open(input_file, "r", encoding="utf-8")
    fout = open(output_file, "w", encoding="utf-8")

    for line in fin:
        reversed_line = line.rstrip()[::-1] #invert car.
        fout.write(reversed_line + "\n")

    fin.close()
    fout.close()


# Exemplu de utilizare
reverse_lines("ex2.txt", "output.txt")
print("Fișierul output.txt a fost creat.")
