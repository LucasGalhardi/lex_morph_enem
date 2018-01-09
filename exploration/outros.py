# selected_pairs2 = []
# for p1 in set(lemmas_and_words_n):
#     cont = 0
#     for p2 in set(lemmas_and_words_n):
#         if p1[0] == p2[0]:
#             cont += 1
#     if cont > 1:
#         selected_pairs2.append(p1)
#
# selected_pairs2 = sorted(selected_pairs2, key=itemgetter(0))


# words_to_search_for_meaning = set(unique_tokens) | set(lemmatized_words_n)
# print(len(words_to_search_for_meaning))
#
# file = open('dic_api/words_to_search_for_meaning.txt', 'a', encoding='utf-8')
# for i in words_to_search_for_meaning:
#     file.write(i + '\n')
# file.close()
