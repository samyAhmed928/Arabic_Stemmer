class fcis_steamer():
    def __init__(self):
        self.Alif_lam_list = [
        "ال",
        "وال",
        "لل",
        "ولل",
        "فال",
        "فل",
        "بال",
        "فبال",
        "كل",
        "كال",
        "فب"
    ]
        self.LAVZ_ELGLALA_list = [
        "بالله",
        "لله",
        "والله",
        "تالله",
        ]
    def remove_ALIF_LAM(self,word):
        for al in self.Alif_lam_list:
            if word.startswith(al):
                word = word[len(al):]
                break
        return word

    def LAVZ_ELGLALA(self,word):
        for al in self.LAVZ_ELGLALA_list:
            if word== al:
                word="الله"
                break
        return word

    def remove_TaaMarbuta(self,word):
        for suffix in [ "هم","ه","ية", "اية", "ة"]:
            if word.endswith(suffix):
                word = word[:-len(suffix)]
                break
        return word
    def remove_ast(self, word):
        if word.startswith("است") or word.startswith("أست"):
            word = word[3:]
            if word[-2] == "ا":
                word = word[:-2] + word[-1]
        return word



    def remove_future_tense_plural(self, word):

        for prefix in ["سي","ست"]:
            for suffix in ["ون", "ان", "ات", "ين"]:
                if word.endswith(suffix)and word.startswith(prefix):
                    word=word[len(prefix):]
                    word = word[:-len(suffix)]
                    break
        return word

    def remove_future_tense_single(self, word):

        if len(word)>=5:

            if word[-1]!="ة":

                for prefix in ["سي", "ست","سأ","سا"]:
                    if word.startswith(prefix):
                       word = word[len(prefix):]
                       break

        return word
    def remove_plural(self, word):
        for suffix in ["ون", "ان", "ات", "ين"]:
            if word.endswith(suffix):
                word = word[:-len(suffix)]
                break
        return word

    def Noun_weights(self,word):
        #new_word = word[:index_to_remove] + word[index_to_remove+1:]
        #الوزن فاعل
        if len(word)==4:
            if word[1]=="ا":
                word=word[:1]+word[2:]
                return  word


        # الوزن تفاعل
        if len(word) == 5:
            if word[0] ==  "ت" and word[2]=="ا":
                word=word[1]+word[3:]
        # الوزن مفعول
        if word[0] == "م" and word[3] == "و":
            word = word[1] + word[2]+word[4]
        if len(word) == 6:
            if word[0]==  "أ" or word[0]=="ا"  and word[2]=="ت" and word[4]=="ا":
               word=word[1]+word[3]+word[5]
            # الوزن انفعال
            if word[0]==  "أ" or word[0]=="ا"   and word[1]=="ن" and word[4]=="ا":
                word=word[2]+word[3]+word[5]
            # الوزن افتعال

        if len(word) == 7:
            # الوزن استفتعال
            if word[0]==  "أ" or word[0]=="ا"  and word[1]=="س" and word[2]=="ت" and word[5]=="ا":
                word=word[3]+word[4]+word[6]
        #الوزن مفعل
        if word[0] == "م":
            word = word[1:]
            return word
        return word

    def verb_weight(self,word):
        if len(word)==4:
            #افعل/أفعل/تفعل
            if word[0]== "أ" or word[0]== "ا" or word[0]== "ت":
                word=word[1:]
        if len(word) == 5:
            #افتعل
            if word[0]== "أ" and word[2]== "ت":
                word=word[1]+word[3:]
            #انفعل
            if word[0]== "أ" and word[1]== "ن":
                word=word[2:]
        return word

    def Convert_to_past(self,word):
        if word.startswith("يست") or word.startswith("تست") or word.startswith("نست"):
            word= "أ" +word[1:]
        if word.startswith("ي") or word.startswith("ت") or word.startswith("ن"):
            word=word[1:]

        return word
    def stem(self,word):
        word=self.LAVZ_ELGLALA(word)
        if word !="الله":
            word = self.remove_ALIF_LAM(word)
            #print("remove_ALIF_LAM" + word)
            word = self.remove_TaaMarbuta(word)
            #print("remove_TaaMarbuta" + word)
            word = self.remove_plural(word)
            #print("remove_plural" + word)
            if len(word)>3:

                word=self.Noun_weights(word)
                #print("Noun_weights"+word)
                word = self.Noun_weights(word)
                #print("Noun_weights" + word)
                word=self.remove_future_tense_single(word)
                #print("remove_future_tense_single" + word)
                word = self.remove_future_tense_plural(word)
                #print("remove_future_tense_plural"+word)

                word=self.Convert_to_past(word)
                #print("Convert_to_past" + word)
                word=self.verb_weight(word)
                #print("verb_weight" + word)
                word = self.remove_ast(word)
                #print("remove_ast"+word)
        return word
def main():
    s = fcis_steamer()
    r = ""
    sentence =input()


    x = ""
    for w in sentence.split():
        x = x + " " + s.stem(w)

    print(r)
    print(x)


if __name__ == "__main__":
    main()