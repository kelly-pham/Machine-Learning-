from recommendation import genres
from math import sqrt
import matplotlib.pyplot as plt       # to draw a plot


# Calculate distance-based similarity using Euclid distance formular: sqrt((a-b) ** 2)
def Euclid_distance(preferences, genre1, genre2):
    share_list={}
    for item in preferences[genre1]:
        if item in preferences[genre2]:
            share_list[item]= 1

    # if they have 0 common return 0
    if len(share_list)== 0:
        return 0

    Sum_of_square=sum([pow(preferences[genre1][item] - preferences[genre2][item],2)
                    for item in preferences[genre1] if item in preferences[genre2]])
    return 1/(1+float(Sum_of_square))

def Pearson(preferences,genre1 ,genre2):
    share_list={}
    for item in preferences[genre1]:
        if item in preferences[genre2]:
            share_list[item]= 1
    if len(share_list) == 0:
        return 0


    n = len(share_list)
    sum1=sum([preferences[genre1][item] for item in share_list])
    sum2 = sum([preferences[genre2][item] for item in share_list])

    sum1_of_square=sum([pow(preferences[genre1][item],2) for item in share_list])
    sum2_of_square=sum([pow(preferences[genre2][item],2) for item in share_list])

    product_sum=sum([preferences[genre1][item] * preferences[genre2][item] for item in share_list])

    #Calculate Pearson
    number=product_sum - (sum1 * sum2 / n)
    den=sqrt((sum1_of_square-pow(sum1,2)/n)  * (sum2_of_square -pow(sum2,2)/n))

    if den==0:
        return 0
    return number/den

def cosin_similarity(preferences,genre1,genre2):
    share_list = {}
    for item in preferences[genre1]:
        if item in preferences[genre2]:
            share_list[item] = 1
    if len(share_list) == 0:
        return 0

    for item in share_list:
        x=preferences[genre1][item]
        y=preferences[genre2][item]

        sumxx = 0
        sumxy = 0
        sumyy = 0

        sumxx += x*x
        sumyy += y*y
        sumxy += x*y

        output = sumxy / sqrt(sumxx * sumyy)
    return output

def main():
    print("\tUsing Euclidean distance method\t")
    object1=Euclid_distance(genres,'Comedy','Romance')
    print('Similarity Score between {} and {}: {:f}'.format('Comedy','Romance',object1))

    object2=Euclid_distance(genres,'Romance','Horror')
    print('Similarity Score between {} and {}: {:f}'.format('Romance', 'Horror', object2))

    print("--------------------------------")
    print("\tUsing Pearson method\t")
    object3=Pearson(genres,'Comedy','Horror')
    print('Similarity Score between {} and {}: {:f}'.format('Comedy', 'Horror', object3))

    object4 = Pearson(genres, 'Romance', 'Horror')
    print('Similarity Score between {} and {}: {:f}'.format('Romance', 'Horror', object4))

    print("--------------------------------")
    print("\t Using Cosine Similarity\t")
    object5=cosin_similarity(genres,'Romance','Horror')
    print('Similarity Score between {} and {}: {:f}'.format('Romance', 'Horror', object5))

if __name__ == '__main__':
    main()