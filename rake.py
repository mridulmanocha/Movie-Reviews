from __future__ import division
import operator
import nltk
import string

def isPunct(word):
  return len(word) == 1 and word in string.punctuation

def isNumeric(word):
  try:
    float(word) if '.' in word else int(word)
    return True
  except ValueError:
    return False

class RakeKeywordExtractor:

  def __init__(self):
    self.stopwords = set(nltk.corpus.stopwords.words())
    self.top_fraction = 1 # consider top third candidate keywords by score

  def _generate_candidate_keywords(self, sentences):
    phrase_list = []
    for sentence in sentences:
      words = map(lambda x: "|" if x in self.stopwords else x,
        nltk.word_tokenize(sentence.lower()))
      phrase = []
      for word in words:
        if word == "|" or isPunct(word):
          if len(phrase) > 0:
            phrase_list.append(phrase)
            phrase = []
        else:
          phrase.append(word)
    return phrase_list

  def _calculate_word_scores(self, phrase_list):
    word_freq = nltk.FreqDist()
    word_degree = nltk.FreqDist()
    for phrase in phrase_list:
      degre = list(filter(lambda x: not isNumeric(x), phrase))
      degree=len(degre)-1
      for word in phrase:
        word_freq[word]+=1
        word_degree[word]+=1
        word_degree[degree]+=1
    for word in word_freq.keys():
      word_degree[word] = word_degree[word] + word_freq[word] # itself
    # word score = deg(w) / freq(w)
    word_scores = {}
    for word in word_freq.keys():
      word_scores[word] = word_degree[word] / word_freq[word]
    return word_scores

  def _calculate_phrase_scores(self, phrase_list, word_scores):
    phrase_scores = {}
    for phrase in phrase_list:
      phrase_score = 0
      for word in phrase:
        phrase_score += word_scores[word]
      phrase_scores[" ".join(phrase)] = phrase_score
    return phrase_scores
    
  def extract(self, text, incl_scores=False):
    sentences = nltk.sent_tokenize(text)
    phrase_list = self._generate_candidate_keywords(sentences)
    word_scores = self._calculate_word_scores(phrase_list)
    phrase_scores = self._calculate_phrase_scores(
      phrase_list, word_scores)
    sorted_phrase_scores = sorted(phrase_scores.items(),
      key=operator.itemgetter(1), reverse=True)
    n_phrases = len(sorted_phrase_scores)
    if incl_scores:
      return sorted_phrase_scores[0:int(n_phrases/self.top_fraction)]
    else:
      return map(lambda x: x[0],
        sorted_phrase_scores[0:int(n_phrases/self.top_fraction)])

def extractphrases(data):
  rake = RakeKeywordExtractor()
  keywords = rake.extract(data, incl_scores=True)
  return keywords
#  
#if __name__ == "__main__":
#    data=""""Spoiler free review. Let me first start of by saying that I am not a Marvel ''fanboy'' or a DC nerd. The comic book genre of films have made it to my personal top 3 favourite genres in the last decade and the MCU has been a strong contributor to that rise. I hold the first Ironman, first Avengers and Captain America 1+2 in high regard. I did not like the direction they took with Iron Man 3 (more on this below) or Guardians of the Galaxy but Winter Soldier was a gem in terms of balancing solid action, drama and levity.
#    That being said, my initial thoughts on Age of Ultron (AoU) are quite negative. To me, its essentially a carbon copy of IM3. There are problems which strike you repeatedly as you progress throughout the film. The 2 biggest complaints I have with AoU is 1) the tone (comedy) 2) the script/writing.
#    So starting with the tone. I like to laugh as I'm sure most people do, but there is a time and place to exhibit your comedy writing skills in an action film. In AoU, its a constant, recurring and predictable theme. It's not limited to one character either, everyone is popping one liner jokes as if its the Expendables and yes, most are not funny. The timing of these moments of levity are horrible too, desensitising the viewer to any impending fear of death in battle. If the characters seem so relaxed in not worrying about possibly dying, then what suspense is needed to be held by the audience? This plagued IM3 in a bad way and its arguably worse here. The comic book films which achieved great success in this regard were XMen DOFP, The Avengers 1, Cap 2 even Dark Knight Rises! Can you imagine at the climax of Xmen DOFP if old Magneto and Storm and Bishop start pulling one liner jokes as the army of sentinels came charging at them? It would kill any tension! 2) The script. I won't say too much since this is a spoiler free review, but it really feels rushed and unorganised. I watched Fast 7 around 2 weeks before AoU and I got similar vibes. Again, its not the fact that the film is 2.5 hours long or has too many characters, that isn't am excuse since The Dark Knight and Xmen DOFP shows how to navigate these theatrical obstacles. There are a few completely unnecessary subplots in AoU and useless characters which do not impact the story overall. The villain himself, Ultron is another massive let-down in Marvels already growing catalogue of mishandled villains.
#    So as a summary, if you want mindless action and cool CGI, which this film does offer in the form of some spectacular visual fight scenes then you will like AoU. If you are after a darker, grounded and more moving story like the trailers promised, you will be severely disappointed. Final score 6/10 and I am being kind since Cap is my fav Avenger and they finally gave him some good screen time.
#    """
#    test(data)
#
