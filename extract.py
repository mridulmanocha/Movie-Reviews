#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:45:16 2018

@author: jatin
"""

from rake import extractphrases
from sentencextractor import split_into_sentences
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet


data=""""Spoiler free review. Let me first start of by saying that I am not a Marvel ''fanboy'' or a DC nerd. The comic book genre of films have made it to my personal top 3 favourite genres in the last decade and the MCU has been a strong contributor to that rise. I hold the first Ironman, first Avengers and Captain America 1+2 in high regard. I did not like the direction they took with Iron Man 3 (more on this below) or Guardians of the Galaxy but Winter Soldier was a gem in terms of balancing solid action, drama and levity.
    That being said, my initial thoughts on Age of Ultron (AoU) are quite negative. To me, its essentially a carbon copy of IM3. There are problems which strike you repeatedly as you progress throughout the film. The 2 biggest complaints I have with AoU is 1) the tone (comedy) 2) the script/writing.
    So starting with the tone. I like to laugh as I'm sure most people do, but there is a time and place to exhibit your comedy writing skills in an action film. In AoU, its a constant, recurring and predictable theme. It's not limited to one character either, everyone is popping one liner jokes as if its the Expendables and yes, most are not funny. The timing of these moments of levity are horrible too, desensitising the viewer to any impending fear of death in battle. If the characters seem so relaxed in not worrying about possibly dying, then what suspense is needed to be held by the audience? This plagued IM3 in a bad way and its arguably worse here. The comic book films which achieved great success in this regard were XMen DOFP, The Avengers 1, Cap 2 even Dark Knight Rises! Can you imagine at the climax of Xmen DOFP if old Magneto and Storm and Bishop start pulling one liner jokes as the army of sentinels came charging at them? It would kill any tension! 2) The script. I won't say too much since this is a spoiler free review, but it really feels rushed and unorganised. I watched Fast 7 around 2 weeks before AoU and I got similar vibes. Again, its not the fact that the film is 2.5 hours long or has too many characters, that isn't am excuse since The Dark Knight and Xmen DOFP shows how to navigate these theatrical obstacles. There are a few completely unnecessary subplots in AoU and useless characters which do not impact the story overall. The villain himself, Ultron is another massive let-down in Marvels already growing catalogue of mishandled villains.
    So as a summary, if you want mindless action and cool CGI, which this film does offer in the form of some spectacular visual fight scenes then you will like AoU. If you are after a darker, grounded and more moving story like the trailers promised, you will be severely disappointed. Final score 6/10 and I am being kind since Cap is my fav Avenger and they finally gave him some good screen time.
    
    I have noticed a trend of negative reviews directed at the humor in the movie. Listen...humor is subjective. It's also a big part of these types of movies. When I read someone criticize the movie because the heroes are dropping one-liners during intense fighting scenes and to them, this downplays the seriousness of the situation or shows a lack of concern for safety from our heroes, I shake my head so hard I get dizzy.
    This is a comic book movie! It's a fantasy/fiction/whatever you want to call it! I'm not a comic book expert, but have been a big fan of the Marvel Universe on film since Iron Man 1. I found the writing in AoU to be sharp and witty. And yes, I laughed more than I thought I would. 
    "There's not enough character development!" I've seen this in the negative reviews, too. Look, we've had 3 Iron Mans, 2 Captain Americas, 2 Thors, and a Hulk movie to develop the characters. At this point, there isn't much more we really need, is there? Yes, we see more about Hawkeye's personal side here, but to me, that only feels fair since he's not big enough to carry his own film. And given that he's very much just a human with a great set of physical skills and is less protected and faces his mortality far more than the others do, I felt like it made perfect sense here. We see and learn more about Black Widow in this one, as well. So the complaints about character development don't hold any weight to me. It sounds like the angst of a group of people expecting to see the Empire Strikes Back version of the Avengers. 
    In Age of Ultron, we get immediate, sustained action. I don't know about you, but if I'm going to watch a movie with a cast of characters that have the abilities of the Avengers, I want to see them in action! The creativity of the collaborative fighting was improved as well and was featured much more so than in the first one. That was something that I think the first film lacked, the side by side teamwork. This movie held my attention from start to finish. 
    As my summary says above, Mjollnir is a pleasantly surprising star of the movie. When you watch it, you'll see why and in my opinion, if you don't enjoy its role here, you really just have a bad attitude!
    
    I'll say this: If you don't mind more of the same you'll probably love this movie. If you wanted something different, some change to the Marvel formula, you'll be disappointed. Age of Ultron is pretty much the same movie as the first one. Especially the ending which feels like it follows the first movie beat by beat.
    There are good, fun moments spread all through the movie, don't get me wrong I liked plenty of stuff in it. The romance between Hulk and Black Widow was interesting, this universe has been weirdly sexless so it was nice to see some tension between the characters. But good moments don't make a good movie. What annoyed me in Age of Ultron was how it just glossed over so many things. The story is extremely thin, even for a superhero movie.
    Tony Stark retired in Iron Man 3 and now he's suddenly back? They don't even try to explain his return. Tony Stark also creates Ultron, the main bad guy of the movie who goes to cause some major mayhem. The movie just glosses over the fact that everything is Stark's fault. Aside Hawkeye there isn't any character development. These movies always just seem to be about "setting something up" for the future movies and I think I finally figured it. The only thing they're setting up is more characters running around, bigger CGI punching bigger CGI and bigger thing falling from the sky. In the middle of all this it's just so hard to care about anything. All those previous movies build to this?
    Age of Ultron seems to just be in a hurry and jump over the story and get to the CGI punching CGI and oh boy there's plenty of that. The Avengers fight an army of generic, faceless and harmless CGI robots for 2 hours, roll credits. I just didn't care. There's no stakes in the action. When the characters are just joking around I'm not worried if they'll make it till the next movie.
    Marvel should have gotten serious in Age of Ultron. You can be serious without being all "dark and gritty" too. Joss Whedon said he was influenced by Empire Strikes Back and Godfather Part 2. Joss Whedon promised we'd see some superhero blood. Joss Whedon failed.
    
    There's no one word that can some up this movie. I won't use 'eh' because that's a bit too vague, and I think it's a bit better than that. But things like 'good' or 'amazing' are too crazy to use. Welcome to my review.
    Age of Ultron opens to a fine start -in fact, an amazing start- with a fresh, intense, action-packed sequence. The Avengers are introduced for the sequel, and so are two new characters: Scarlet Witch and Quicksilver. These ended up being my favourite (Yes, I'm spelling it right. I'm not American, y'know) characters in this movie. Unfortunately, they get tossed a side a bit. Considering they're new characters, and considering one is in an upcoming movie and the other dies, they should have gotten more development. I adored Scarlet Witch and her powers, at least in the parts that she's ACTUALLY IN.
    After the opening, everything goes downhill, at least SLIGHTLY. Ultron's introduction is quite terrible. Can anyone explain to me how this invisible force can suddenly SPEAK inside a whole load of technological material? I don't know... It just felt pretty dumb to me. If this was how it was in the comics, then I suppose I can't really complain much. But I guess I could say that it doesn't translate to screen very well. 
    After that, the movie becomes kind of dull. I kept twitching in my seat various different times. If I can say one thing, it's that the action sequences were fantastic, and they're the only things that hold this movie up. Ultron was nothing like he was in the teaser trailer that got me hyped, nor was the movie. I wanted a dark, gritty, intense, heart-breaking, half-horror movie! The advertising for this movie is false, almost to the point where I could sue. Remember Scarlet's gut-wrenching scream, or maybe Ultron saying "There's no strings on me" in the teaser trailer? Well guess what? Nowhere to be found. But there's one last thing that makes me feel at least a bit satisfied with the movie, and that was the last act. When Ultron's plans were finally revealed, everything turned amazing. The CGI effects were absolutely incredible, and there are shots in the trailers that would reveal his plan if they were extended by a few seconds, so keep an eye out...
    By the end of this review, I can finally figure out one word to sum this up. 'Overrated.'
    You can mark this review as unhelpful, but I don't care. It's my opinion. This movie is definitely NOT a must see, but I guess it is for any fans of the comics.
    Just be prepared for a completely different film to the film marketed in the trailers.. Thank you for reading, and I know that at least somebody will agree with me.
    EDIT:
        So I was sippy sipping on my mug of tea and I almost spat it out all over my screen. This movie is rated 7.9. I have now changed my 6/10 rating to 1/10 simply to try and lower the rating to what it deserves. 
        Before you Marvel nerds attack me, I am doing this because this movie is average at most. You are crazy if you rate it higher than 6.
        Goodbye.
    
    Avengers age of Ultron is by far the best Marvel movie to date. It has all the elements of the first movie, but steps it up in the action, character and dialog. I went into this movie with very unrealistically high expectations. So when I saw this movie, I was very worried but excited. 
    All the cast from the previous Avengers movie all reprise their roles. Robert Downey Juinor was amazing as Ironman. Chris Evans and Chris Hemsworth were both great as Captain America and the mighty Thor. Scarlett Johanson was brilliant as Black Widow and was even more bad-ass in this movie, than any of her other films. Her role was substantially bigger this time around. This can also be said about Hawkeye, who's role was way bigger in this movie. In fact, Hawkeye even has some of the best lines and the best action sequences. Mark ruffilo was once again amazing as Hulk and Bruce Banner. The one character that stole the show, would be James Spader. He embodies an evil AI robot perfectly. He can be really calm and yet menacing and sometimes he can be full of rage and anger. Aron Taylor Johnson and Elisibeth Olsin are also a great new edition to the marvel universe. The scarlet Witch character has a big part in the film also.
    The action has been dialed up and the set pieces are bigger and better. The cgi can seem a little off at times, but other than that, it looks fantastic.
    The movie also spends time on the relationships and past of some characters, which leads to some great character moments. This is much more emotional, than the first movie. I would defiantly say that this movie is better than the first Avengers Movie!
    
    Well, the superhero movies have sucked their last dollar out of me. I don't like watching movies just to see things blown up. The writers and director are so much into showing off their destructive action sequences that they didn't pause to consider whether soneone would actually give an F. Superthin plot. The occasional quip grom Ultron or an Avenger gets old quick with nothing else to support it. We're clearly dealing with high school humor here. I really like the scene where the earth is caving in, thousands of people obviously meeting gruesome deaths, and yet a few Avengers take the time to save one woman in a falling vehicle...NOT.
    """
 
words=nltk.tokenize.wordpunct_tokenize(data)

finalwords=[]
for x in words:
    if not wordnet.synsets(x):
        continue
    else:
        if x.__len__()>3 and not str.isnumeric(x):
            finalwords.append(x)
    
phrases=extractphrases(data)
final=[]
for x in phrases :
    final.append(x[0])
    

temp=split_into_sentences(data)

for x in temp:
    final.append(x)



file = open("phrases.txt", "w",encoding='utf-8')

finallist=[]
sid = SentimentIntensityAnalyzer()
for sentence in final:
    temp=[]
    temp.append(sentence)
    ss = sid.polarity_scores(sentence)
    temp.append(ss['compound'])
    finallist.append(temp)
    s=sentence+' '+str(ss['compound'])+'\n'
    file.write(s)
    
file.close()

file=open("words.txt",'w',encoding='utf-8')

sid = SentimentIntensityAnalyzer()
for word in finalwords:
    ss = sid.polarity_scores(word)
    temp.append(ss['compound'])
    s=word+' '+str(ss['compound'])+'\n'
    file.write(s)
    
file.close()

         
print("Writing complete")