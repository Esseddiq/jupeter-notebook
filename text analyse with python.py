rowdata="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class Textanalyzer:
    def __init__(self,text):
        formatedtext=text.replace('.','').replace('!','').replace('?','').replace(',','')
        formatedtext=formatedtext.lower()
        self.fmtext=formatedtext
    def freqall(self):
        wordslist=self.fmtext.split(' ')
        freqdic={}
        for word in set(wordslist):
            freqdic[word]=wordslist.count(word)
        return freqdic
    def freqofword(self,word):
        freqofone= self.freqall()
        if word in freqofone :
            return freqofone[word]
        else:
            return 0
analyze1=Textanalyzer(rowdata)
formated=analyze1.fmtext
print(f"text formated successfuly:{formated}")
freqofall=analyze1.freqall()
print(f"the frequene of all words as fallow: {freqofall}")
word='el'
frequency=analyze1.freqofword(word)
print(f"the {word} is repeated {frequency} times")