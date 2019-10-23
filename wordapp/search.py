# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:44:56 2019

@author: 212764757
"""


import operator

word_frequency = {}
list_of_words = []
with open('word_search.tsv') as datafile:
	for each_row in datafile:
		word, frequency = each_row.split('\t') 			#dividing it into word and frequency of occurence
		word_frequency[word] = int(frequency.strip())	#inserting into the wordcount dictionary key as word and value as frequency
		list_of_words.append(word)							#inserting only the word in words

#Search function to search for the (partial) word in any word of words list.
def search(partial):
	search_results = []
	for item in list_of_words:
		if partial in item:
			search_results.append(item)
	return search_results


def prioritizing(search_results, partial):
    priority=[]
    for item in search_results:
        priority.append([item,item.find(partial),word_frequency[item],len(item)]) #creating a list of lists with words containing the partial word and their frequency, starting index and length 
    priority.sort(key=operator.itemgetter(1)) #sorting based on starting index
    priority.sort(key=operator.itemgetter(3)) #sorting based on length
    refined_search_results=[]
    count=0
    for item in priority:
        if(count<25):
            refined_search_results.append(item[0])
            count+=1
    return refined_search_results