languages = []

for i in range(5):
    language = input("Programming languages: ")
    languages.append(language)

print()

languages.sort()

print("Languages:")

for language in languages:
    print(language)

