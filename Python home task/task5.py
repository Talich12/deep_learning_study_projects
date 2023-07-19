def process(sentences):
    delete = False
    result = []
    for i in sentences:
        i = i.split(' ')
        for j in i:
            for k in j:
                if k.isnumeric() or not (k.isalpha() or k.isdigit() or k == ' '):
                    delete = True
                    break
            if delete:
                i.remove(j)
                delete = False
        if len(i) != 0:
            result.append(' '.join(i))
    return result

# Задание не выполнено, не получилось реализовать проверку на спец символы, пытался разными способами но не получилось
# Хотел сделать проверку через from string import punctuation, но подумал что нельзя ничего импортировать и отказался от этой идеи

# Ага, хорошие предложения по проверке. 
# В целом у python очень богатая встроенные библиотеки и методы объектов.
# у python string есть полезный встроенный метод 'string'.isalpha().
# Я делал так, задание сдается )
# Если будут вопросы по коду, - пиши разберем )

# def process(sentences):
#     result = []
#     for text in sentences:
#         result.append(' '.join(list(filter(lambda x : x.isalpha(), text.split()))))

#     return result