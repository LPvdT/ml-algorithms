# Algorithm: K Nearest Neighbors

import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbors(data, predict, k):
	if len(data) >= k:
		warnings.warn('K is set to a value less than total voting groups, moron.')

	distances = []

	for group in data:
		for features in data[group]:
			euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
			distances.append([euclidean_distance, group])

	votes = [i[1] for i in sorted(distances) [:k]]
	vote_result = Counter(votes).most_common(1)[0][0]
	confidence = Counter(votes).most_common(1)[0][1] / k

	return vote_result, confidence

accuracies = []

#Run test i times
for i in range(21):

	df = pd.read_csv("data/breast-cancer-wisconsin.data.txt")
	df.replace('?', -99999, inplace = True)
	df.drop(['id'], 1, inplace = True)
	full_data = df.astype('float').values.tolist()

	#Shuffle data
	random.shuffle(full_data)

	#Define size and set dictionaries
	test_size = 0.2
	train_set = {2:[], 4:[]}
	test_set = {2:[], 4:[]}

	#Slice data
	train_data = full_data[:-int(test_size * len(full_data))]
	test_data = full_data[-int(test_size * len(full_data)):]

	#Populate dictionaries
	for i in train_data:
		train_set[i[-1]].append(i[:-1])

	for i in test_data:
		test_set[i[-1]].append(i[:-1])

	#Run algorithm and count accuracy
	correct = 0
	total = 0

	for group in test_set:
		for data in test_set[group]:
			vote, confidence = k_nearest_neighbors(train_set, data, k = 5)
			if group == vote:
				correct += 1
			total += 1

	#print('Accuracy:', correct/total)
	accuracies.append(correct/total)

#Print average accuracy over test size iterations
print('Mean accuracy:', sum(accuracies) / len(accuracies))