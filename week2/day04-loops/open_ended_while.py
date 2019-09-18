from random import choice

def get_sample(lower=1, upper=100):
    return choice(range(1, upper+1))

def get_sample_counts(m, threshold):
    output = []

    for _ in range(m):
        num_trials = 1
        while True:
            sample = get_sample()

            if sample < threshold:
                output.append(num_trials)
                break
            else:
                num_trials += 1

    return output


sample_trials = get_sample_counts(100, 25)

# we will make the index of counts correspond with the
# number of trials
counts = [0]*(max(sample_trials) + 1)

for trial in sample_trials:
    counts[trial] += 1

# we'll make a terminal graphic to display the distribution of number of trials needed to achieve a value below a given threshold.
for i, count in enumerate(counts):
    if i == 0:
        continue
    print('{:4d}: {}'.format(i, '*' * count))