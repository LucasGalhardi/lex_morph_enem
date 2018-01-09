import json

file_in_json = json.loads(open('essays.json').read())

set_of_prompts = set()

for i in file_in_json:
    if i['type']=='essay':
        set_of_prompts.add(i['prompt'])

dict_of_prompts = {}
cont = 0
for pt in set_of_prompts:
    # print(pt)
    cont+=1
    dict_of_prompts[pt] = cont

# for v in dict_of_prompts.items():
#     print(v)
for v in dict_of_prompts.keys():
    cont = 0
    palavras = 0
    for i in file_in_json:
        if i['type']=='essay':
            if i['prompt']==v:
                palavras += len(i['text'].split())
                cont += 1
    # print(v + " has " + str(cont) + " essays, with " + str(palavras) + " words in total.")

total = 0
qtdade = 0
for i in file_in_json:
    if i['type']=='essay':
        # if i['text'] != '':
        total += len(i['text'].split())
        qtdade += 1
print("media de palavras nas redacoes eh: " + str(total/qtdade))

redacoes_sociedade_meio_ambiente = {}
cont = 0
for i in file_in_json:
    if i['type']=='essay':
        if i['prompt']=='http://vestibular.brasilescola.uol.com.br/banco-de-redacoes/tema-sociedade-x-meio-ambiente.htm':
            cont += 1
            redacoes_sociedade_meio_ambiente[str(cont)] = i['text']
            # print(i['title'])
            # print(i['text'])

# print(redacoes_sociedade_meio_ambiente)

total_palavras = 0
for i in redacoes_sociedade_meio_ambiente.values():
    total_palavras += len(i.split())
# print(str(total_palavras))

# type,prompt,title, description,info,url,date, text
# print("type = " + file_in_json[1]['type'])
# # print(file_in_json[1]['prompt'])
# print(file_in_json[1]['title'])
# print(file_in_json[1]['description'])
# print(file_in_json[1]['info'])
# print(file_in_json[1]['url'])
# print(file_in_json[1]['date'])
# print(file_in_json[1]['text'])
