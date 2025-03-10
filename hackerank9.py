if __name__ == '__main__':
    records = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)
    
    second_lowest = sorted(scores)[1] 

    names = sorted([name for name, score in records if score == second_lowest]) 
    
    for name in names:
        print(name)  
