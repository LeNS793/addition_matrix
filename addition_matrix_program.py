# ввод исходного текста, соответствующего шифра, фразу, которую требуется зашифровать, расшифровать,
# шаг разбивки строк
first_input, second_input, phrase, phrase_decoding, n = input(), input(), input(), input(), 1

# разбивка строк в списки по отдельному элементу
alphabet = [first_input[i:i+n] for i in range(0, len(first_input), n)]
cipher = [second_input[i:i+n] for i in range(0, len(second_input), n)]
# print(alphabet, cipher

# создание двух словарей: d для шифрования, reverse_d для расшифровки;
# для d alphabet[i]- ключи, ciper[i] - значения; для reverse_d наоборот
d = dict(zip(alphabet, cipher))
reverse_d = dict(zip(cipher, alphabet))

# вывод значений словарей по ключам на экран
for i in phrase:
    print(d[i], end='')
print()

for i in phrase_decoding:
    print(reverse_d[i], end='')