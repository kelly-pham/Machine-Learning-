
from operator import itemgetter
# list of recommendation movies based on genres, listed on website www.imdb.com

genres= {'Comedy':{'Jumanji':7.3 , 'Shameless' : 8.7,'Pitch Perfect 3': 6.3,'Lady Bird': 8.1,
            'Disaster Artist':7.9},
         'Romance':{'The Greatest Showman':8.0,'The shape of water':8.2,'Call me by your name': 8.4,
                    'Beauty and the Beast': 7.3,'Pitch Perfect 3': 6.3,'Lady Bird': 8.1,'Shameless' : 8.7},
         'Horror':{'IT':7.6,'Insidious':6.1,'Get out':7.7,'Mother':6.8,'The Killing of Sacred Deer':7.3,
                   'Mom and Dad':6.5,'The shape of water':8.0}
        }

def switch_product(preferences):
    movie_list ={}
    for genre in preferences:
        for item in preferences[genre]:
            movie_list.setdefault(item,{})
            movie_list[item][genre]=preferences[genre][item]
    return movie_list


output =(switch_product(genres))      #switching genres and movie titles
sort_key=(sorted(output.keys()))        # sort movie titles alphabetically

list2=([(key,value) for key,value in output.items()])       # expand movie list dictionary to list
print(list2)                                                # print out list

