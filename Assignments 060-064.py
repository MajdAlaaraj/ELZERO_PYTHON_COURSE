# Assignment 1
def get_score(**scores) :
    for score_key , score_val in scores.items():
        print(f"{score_key} => {score_val}")



get_score(math=90,geography=75,language=100)


#Assignment 2
def get_score(name,**scores) :
    if len(scores) == 0 :
        print(f"Hello {name} You Have No Scores To Show.")
    else :
        print(f"Hello {name} This Is Your Scores Table :")
        for score_key ,score_val in scores.items() :
            print(f"{score_key} => {score_val}")

get_score("ahmad",math=97)


# Assignment 3 :
def get_the_scores(name=0 , **scores_list):
    if len(scores_list) == 0 :
        print(f"Hello {name} You Have No Scores To Show.")
    else :
        if name == 0 :
            for score_key ,score_val in scores_list.items() :
                print(f"{score_key} => {score_val}")
        else :
            print(f"Hello {name} This Is Your Scores Table :") 
            for score_key ,score_val in scores_list.items() :
                print(f"{score_key} => {score_val}")  
get_the_scores("ahmad",math=80,geo=88)
print("#"*40)
get_the_scores(arabic=70,Eng=88)
print("#"*40)
get_the_scores("majd")
print("#"*40)






