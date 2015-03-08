__author__ = 'Don'
import wolframalpha

def translate_english_to_language (word, language):
    word = word.lower()
    eng_to = word+" from english to "+language
    client = wolframalpha.Client('3X8WHP-6EV4Q5KJ9T')
    res = client.query(eng_to)
    for pod in res.pods:
        if "translate" in pod.text:
            pass
        else:
            return pod.text

def clean_answer(answer):
    answer = answer.split("|")

    for i in answer:
        if "(" in i or ")" in i:
            answer[answer.index(i)] = i.split(" ")
            
    for j in answer:
        for k in j:
            if "(" in k or ")" in k:
                j.remove(k)
    
    for i in range(0, 4):
        for j in answer:
            for k in j:
                if len(k) == 0:
                    j.remove(k)

    for i in answer:
        answer[answer.index(i)] = "".join(i)

    answer = [i.strip() for i in answer]

    for i in answer:
        if ')' in i:
            temp = answer[answer.index(i)]
            answer = temp[temp.index(')')+1:]
    return(answer)


