# Represent a small bilingual (English-Swedish) glossary given below as a python dictionary
# ("merry":"god":"christmas":"jul":"and":"och":"happy":"gott":"new":"nytt":"year":"ar")
# and use it to translate your christmas wishes from english into swedish.
# That is write a python function translate() that accepts the billingual dictionary and a listof english words 
# ( your christmas  wish) and returns a list of equivalent Swedish words.
bilingual_dict = { "merry": "god","christmas": "jul","and": "och","happy": "gott","new": "nytt","year": "år"}
def translate(bilingual_dict, english_words):
    swedish_words = []
    for word in english_words:
        if word in bilingual_dict:
            swedish_words.append(bilingual_dict[word])
    return swedish_words

english_words = ["merry", "christmas", "and", "happy", "new", "year"]
swedish_words = translate(bilingual_dict, english_words)
print(swedish_words)
