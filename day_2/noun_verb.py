import day_2


results = [(day_2.main(i, j)) for i in range(100) for j in range(100)]

nounverb = [i for i, value in enumerate(results) if value == 19690720]

print(nounverb[0])
