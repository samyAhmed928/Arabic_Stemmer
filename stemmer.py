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