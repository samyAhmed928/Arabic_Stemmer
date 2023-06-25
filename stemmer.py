class fcis_steamer():
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