def simulate(secret, steps):
	prices = [secret % 10]
	change_in_prices = [None]
	for _ in range(steps):
		secret = (secret ^ (64 * secret)) % 16777216
		secret = (secret ^ (secret // 32)) % 16777216
		secret = (secret ^ (secret * 2048)) % 16777216
		prices.append(secret % 10)
		change_in_prices.append(prices[-1] - prices[-2])

	return secret, prices, change_in_prices


with open('input.txt') as f:
	data = [int(x.strip()) for x in f.readlines()]

p1 = 0
sequences = {}
for buyer in data:
	secret, prices, change_in_prices = simulate(buyer, 2000)
	seen = set()
	for i in range(len(change_in_prices) - 3):
		sequence = change_in_prices[i:i + 4]
		k = tuple(sequence)
		if k in seen:
			continue

		seen.add(k)
		sequences[k] = sequences.get(k, 0) + (prices[i + 3] or 0)

	p1 += secret

print(p1)
print(max(sequences.values()))
