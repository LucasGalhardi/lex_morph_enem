# for word in dword_list3:
#     print(Fore.BLUE)
#     print("Palavra: " + Fore.GREEN + word.word + Fore.BLUE)
#     tag = word.pos_tag.pop()
#     print("Classe: " + Fore.GREEN + tags_dict.get(tag, '') + Fore.BLUE)
#     word.pos_tag.add(tag)
#     print("Frequência: " + Fore.GREEN + str(word.freq) + Fore.BLUE)
#     print("Raiz: " + Fore.GREEN + word.root + Fore.BLUE)
#     print("Sufixo: " + Fore.GREEN + word.suffix + Fore.BLUE)
#     print(Fore.BLUE, end='')
#     if tag == 'NOUN':
#         print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
#         print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
#         print("Grau: " + Fore.GREEN + grau_dict.get(word.grau, '') + Fore.BLUE)
#     elif tag == 'ADJ':
#         print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
#         print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
#         print("Grau: " + Fore.GREEN + grau_dict.get(word.grau, '') + Fore.BLUE)
#     elif tag == 'VERB':
#         print(Fore.GREEN, end='')
#         if word.pessoa == 'i' and word.numero == 'i' and word.tempo == 'i':
#             print("Verbo no infinitivo")
#             print(Fore.BLUE, end='')
#         elif word.pessoa == 'g' and word.numero == 'g' and word.tempo == 'g':
#             print("Verbo no gerúndio")
#             print(Fore.BLUE, end='')
#         elif word.pessoa == 'p' and word.numero == 'p' and word.tempo == 'p':
#             print("Verbo no particípio")
#             print(Fore.BLUE, end='')
#         else:
#             print(Fore.BLUE, end='')
#             print("Pessoa: " + Fore.GREEN + word.pessoa + "ª" + Fore.BLUE)
#             print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
#             print("Tempo: " + Fore.GREEN + tempo_dict.get(word.tempo, '') + Fore.BLUE)
#     elif tag == 'PRON':
#         print("Número: " + Fore.GREEN + numero_dict.get(word.numero, '') + Fore.BLUE)
#         print("Pessoa: " + Fore.GREEN + word.pessoa + "ª" + Fore.BLUE)
#         print("Gênero: " + Fore.GREEN + genero_dict.get(word.genero, '') + Fore.BLUE)
#     print(Style.RESET_ALL, end='')
#     print("----------------------------------------------------------------", end='')
#     continue
