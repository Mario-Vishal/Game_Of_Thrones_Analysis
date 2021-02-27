class emotions:
    
    def fear(self):

        return ["concerned","concern","fear","fearful","help","forgive","pardon","please",
            "chance","not","again","beg","begged","nothing","alarm","alarmed","aghast",
            "awed","away","don","mercy","shock","shocked","death","dying","lost","spare","sire",
            "life","backdown","killing","killed","disowned","demolished","sensitive",
            "apprehensive","aghast",'aghast', 'alarmed', 'awed', 'cautious', 
            'chicken', 'cowardly', 'defenseless', 'dismayed', 'doubtful', 'exposed', 
            'fainthearted', 'fearful', 'frightened', 'hesitant', 'horrified', 'hysterical', 'in fear', 
            'insecure', 'irresolute', 'menaced', 'misgiving', 'nervous', 'panicked', 'phobic', 'quaking',
            'restful', 'scared', 'shaky', 'suspicious', 'terrified', 'terrorized', 'threatened', 'timid',
            'timorous', 'tremulous', 'upset', 'worried','greyscale', 'afraid', 'attacked', 'diffident',
            'fidgety', 'petrified', 'trembling','disrespect','greyscale','grayscale','unsullied','dothraki',
            'wildlings','sellsword','dreadful','faceless','pleaded','casted','watch','wall',
            'walkers','disfigured','died','popping','fire','monster','animals',
            'fox','beast','dragons','debt','worship','depressed','unhappy','despair','lonely','alone']
    def aggressive(self):
        
        return ['kill','murder','rape','raped','throat','intestine','punch','cut','die','judged','law','rights'
            'dead','crush','boil','boiling','killed','fuck','fucked','fucking','monster','beast','all','irritate','push','pushed','punched','kicked',
            'thrown','head','murderous','bitch','cruel','fire','burn','poke','slice','break','give','everything','useless','shit','don','arouse',
            'challenge','champion','roll','bitter','slash','crunched','crunch',
            'creep','starks','one','angry', 'annoyed', 'appalled','sex', 'bitter', 'boiling', 'cross', 'disgusted', 'enraged',
            'frustrated', 'fuming', 'furious', 'incensed', 'indignant', 'inflamed', 'irate', 'irritated', 'livid','dracaris'
            ,'mad', 'offended', 'outraged', 'provoked', 'rageful', 'resentful', 'sullen', 'up in arms','wrath','destruction','demon',
            'virulent', 'wrathful', 'wrought up', 'acrimonious', 'devastated', 'hostile', 'infuriated', 'piqued', 'worked up','knife','swords',"sword","axe",'sharp','bastard','slut','cum','spit','blood','sacrifice',"curcify","hang","hanged","needle",'red','devour']
    
    def caring(self):
        return ["save","protect","please","release","give","offered","offer","saved","protected","forgived","merciful","people","family","darling","beautiful","care",
            'will','chains','breaker','protector','saviour','child','children','delightful',"delighted","granted","grant",'father','provide','support','encourage','supported','encouraged',
            'love','loving','caring','liking','live','flowers','birds','little','alive','leaving','leave','forgiven','stand','fight','supportive','careful','adorable','entrused','entrust','believe','adored','approved','validated','welcome','welcomed']

    def happy(self):
        return ["happy","nice",'wow','wonderful','great','good','smile','laughing','laugh','smirk','thanks','thankful','debt','calm','peace','peacefull','forgave','happiness','greatness','win','won',
            'proud','pride','respect','think','aww','beautiful','beauty','children','child','satisfied','satisfy','terrific','dance','saved','music','song','honey','darling','apetising','apetiser',
            'dedicated','love','sweet','lovely','kiss','acheived','gold','received','amused', 'animated', 'beatific', 'blissful', 'blithe', 'bright', 'brisk', 'cheerful', 'cheery', 'comfortable', 'contented', 'convivial', 
            'ecstatic', 'elated', 'enthusiastic', 'exhilarated', 'festive', 'free & easy', 'frisky', 'genial', 'glad', 'gleeful', 'happy', 'high-spirited', 'hilarious', 'humorous', 'important', 'jaunty', 'jocular', 'jolly',
             'jovial', 'joyful', 'joyous', 'jubilant', 'lighthearted', 'lively', 'lucky', 'merry', 'mirthful', 'overjoyed', 'peaceful', 'playful', 'pleased', 'proud', 'rapturous', 'satisfied', 'saucy', 'serene', 'sparkling',
              'sprightly', 'sunny', 'thankful', 'tranquil', 'transported', 'vivacious', 'airy', 'buoyant', 'debonair', 'exultant', 'great', 'inspired', 'laughting', 'self-satisfied', 'terrific','child','delightful','fragrance']
        
    def stopWords(self):
        return ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
        'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
         'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 
         'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
          'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', 
          "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]