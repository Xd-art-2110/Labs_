# TODO решите задачу
import json
def task(filename) -> float:
    result = []
    scht = 0
    proiz = 1
    with open(filename) as f:
        data = json.load(f)
        for i in range(len(data)):
            for key in data[i].values():
                if scht % 2 == 0:
                    proiz = key
                    scht += 1
                else:
                    proiz *= key
                    result.append(proiz)
                    scht += 1
    return sum(result)
print(round(task('input.json'), 3))
