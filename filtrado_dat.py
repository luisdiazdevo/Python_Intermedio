from ast import Lambda


DATA = [  #esto es una constante porque esta definido por mayusculas
    {
        'name': 'Facundo',      #Esto es una lista anidando diccionarios
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run ():
    all_python_devs = [worker["name"] for worker in DATA if worker['language'] == "python" ]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]== "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    search_lorenas = list(filter(lambda worker: worker["name"]=="Lorena", DATA))
    adult_name = list(map(lambda worker : worker["name"], adults))
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"]>70}},DATA )) #Pipe es solo 3.9 es unir un diccionario con otro "|"
    
    python_devs = list(filter(lambda worker : worker["language"]=="python", DATA))
    platzi_worker = list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    #for worker in all_python_devs:
        #print(worker)
        
    #for worker in all_platzi_workers:
        #print(worker)
    
    #for workername in adult_name:
        #print(workername)
        
    #for worker in old_people:
        #print(worker)
    
    #for workerpy in python_devs:
        #print(workerpy["name"])
    for workerplatzi in platzi_worker:
        print(workerplatzi["name"], "-", workerplatzi["organization"] )


if __name__ == "__main__":
    run()