#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:51:53 2018

@author: jatin
"""

import re
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences



data=""""Spoiler free review. Let me first start of by saying that I am not a Marvel ''fanboy'' or a DC nerd. The comic book genre of films have made it to my personal top 3 favourite genres in the last decade and the MCU has been a strong contributor to that rise. I hold the first Ironman, first Avengers and Captain America 1+2 in high regard. I did not like the direction they took with Iron Man 3 (more on this below) or Guardians of the Galaxy but Winter Soldier was a gem in terms of balancing solid action, drama and levity.
    That being said, my initial thoughts on Age of Ultron (AoU) are quite negative. To me, its essentially a carbon copy of IM3. There are problems which strike you repeatedly as you progress throughout the film. The 2 biggest complaints I have with AoU is 1) the tone (comedy) 2) the script/writing.
    So starting with the tone. I like to laugh as I'm sure most people do, but there is a time and place to exhibit your comedy writing skills in an action film. In AoU, its a constant, recurring and predictable theme. It's not limited to one character either, everyone is popping one liner jokes as if its the Expendables and yes, most are not funny. The timing of these moments of levity are horrible too, desensitising the viewer to any impending fear of death in battle. If the characters seem so relaxed in not worrying about possibly dying, then what suspense is needed to be held by the audience? This plagued IM3 in a bad way and its arguably worse here. The comic book films which achieved great success in this regard were XMen DOFP, The Avengers 1, Cap 2 even Dark Knight Rises! Can you imagine at the climax of Xmen DOFP if old Magneto and Storm and Bishop start pulling one liner jokes as the army of sentinels came charging at them? It would kill any tension! 2) The script. I won't say too much since this is a spoiler free review, but it really feels rushed and unorganised. I watched Fast 7 around 2 weeks before AoU and I got similar vibes. Again, its not the fact that the film is 2.5 hours long or has too many characters, that isn't am excuse since The Dark Knight and Xmen DOFP shows how to navigate these theatrical obstacles. There are a few completely unnecessary subplots in AoU and useless characters which do not impact the story overall. The villain himself, Ultron is another massive let-down in Marvels already growing catalogue of mishandled villains.
    So as a summary, if you want mindless action and cool CGI, which this film does offer in the form of some spectacular visual fight scenes then you will like AoU. If you are after a darker, grounded and more moving story like the trailers promised, you will be severely disappointed. Final score 6/10 and I am being kind since Cap is my fav Avenger and they finally gave him some good screen time.
    """
temp=split_into_sentences(data)