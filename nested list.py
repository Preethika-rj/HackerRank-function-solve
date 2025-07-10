if __name__ == '__main__':
    
    scores_list = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_list.append(score)
        records.append([name,score])
    
    sorted_scores = sorted(set(scores_list))
    second_highest = sorted_scores[1]
    
    records.sort()
    
    for element in records:
        if element[1] == second_highest:
            print(element[0])