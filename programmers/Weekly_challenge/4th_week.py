def solution(table, languages, preferce):
    answer=''
    job_language = {}
    for job in table:
        temp = job.split()
        job_language[temp[0]] = {}
        for i,j in zip(range(1,6),reversed(temp[1:])):
            job_language[temp[0]][j] = i
    arr = []
    for job in job_language:
        tmp = 0
        for l,score in zip(languages,preferce):
            if l in job_language[job].keys():
                tmp += score * job_language[job][l]
        arr.append(tmp)
    prefer = max(arr)
    job = []
    print(arr)
    for i in range(len(arr)):
        if prefer == arr[i]:
            job.append(list(job_language.keys())[i])
    if len(job) > 1:
        job = sorted(job)

    return job[0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
language = ["PYTHON", "C++", "SQL"]
preference = [7,5,5]
print(solution(table,language,preference))

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
language = ["JAVA", "JAVASCRIPT"]
preference = [7,5]
print(solution(table,language,preference))