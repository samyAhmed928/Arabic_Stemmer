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