import nltk


alice = nltk.corpus.gutenberg.words("carroll-alice.txt")
alice_fd = nltk.FreqDist(alice)
moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
moby_fd = nltk.FreqDist(moby)

print(alice_fd['Rabbit'])

print(alice_fd.most_common(10))

print(alice_fd.hapaxes())

alice_fd_100 = alice_fd.most_common(100)
moby_fd_100 = moby_fd.most_common(100)

alice_100 = [word[0] for word in alice_fd_100 ]
moby_100 = [word[0] for word in moby_fd_100 ]

x = set(alice_100) - set(moby_100)