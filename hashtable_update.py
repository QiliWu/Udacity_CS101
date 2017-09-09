# -*- coding: utf-8 -*-

def hashtable_update(htable,key,value):
    # Your code here
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1]=value
            break
    else:  # if not hit break, the else
        bucket.append([key,value])
    return htable

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

print hashtable_update([[['Francis', 13], ['Ellis', 11]], [['Andy', 5]], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]], 'Francis', 7)

print hashtable_update([[['search', 'verb']], [], [['Peter', 'proper noun']],
                        [['Udacity', 'super noun']], [['with', 'preposition']]],
                       'Udacity', 'proper noun')

print hashtable_update([[['Francis', 13], ['Ellis', 11]], [['Andy', 5]], [['Bill', 17], ['Zoe', 14]],
                        [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]], 'Luke', 7)