'''
Given a list of phrases, write a function that returns a dictionary consisting of
distinct case-insensitive words and how many times they appear in total.

Note: Do not worry about punctuations for now.


'''


from typing import List, Dict

def build_vocab(corpus: List[str])  -> Dict[str, int]:
    word_counter = {}
    
    # Write your code here
    for l in corpus:
        for word in l.split(' '):
            if not word.lower() in word_counter:
                word_counter[word.lower()] = 1
            else:
                word_counter[word.lower()] = word_counter[word.lower()] + 1
    
    
    return word_counter


test_input = [
"A quiet house is nice until you are ordered to stay in it for months.",
"It took him a while to realize that everything he decided not to change, he was actually choosing.",
"Nothing seemed out of place except the washing machine in the bar.",
"Where are you going?",
"Grape jelly was leaking out the hole in the roof.",
"Being unacquainted with the chief raccoon was harming his prospects for promotion.",
"Nancy was proud that she ran a tight shipwreck.",
"She looked into the mirror and saw another person.",
"The lake is a long way from here.",
"What kind of sentence are you looking for anyway?",
"The fish listened intently to what the frogs had to say.",
"When transplanting seedlings, candied teapots will make the task easier.",
"How big of an idiot are you?",
"The lyrics of the song sounded like fingernails on a chalkboard.",
"The sky is clear; the stars are twinkling.",
"Abstraction is often one floor above you.",
"He excelled at firing people nicely.",
"Has he come to get you yet?",
"The golden retriever loved the fireworks each Fourth of July.",
"We will not allow you to bring your pet armadillo along.",
"Hit me with your pet shark!",
"She used her own hair in the soup to give it more flavor.",
"The tree fell unexpectedly short.",
"He's in a boy band which doesn't make much sense for a snake.",
"Is that a pencil?"
]



print(build_vocab(test_input))