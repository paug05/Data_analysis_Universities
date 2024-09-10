
def print_text_file_split_by_comma(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            val1 = []
            val2 = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 1:
                     val1.append(parts[0])
                     val2.append("")
                if len(parts) >= 2:
                    val1.append(parts[0])
                    val2.append(parts[1])
            f = open('neuspalte.txt','a')
            for elements in val1:
                 f.write(elements)
                 f.write("\n")
            f.write("\n")
            for elements in val2:
                 f.write(elements)
                 f.write("\n")
            f.close



print_text_file_split_by_comma('spalten.txt')