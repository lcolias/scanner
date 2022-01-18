class codes:
    lookup_codes = ["!accept", "grave", "leftbracket", "rightbracket", "leftbrace", "rightbrace", "leftsquig",
                    "rightsquig", "atsymbol", "ampersand", "pound", "bang", "tilde", "singlequote", "doublequote" ,
                    "dollarsign", "colon", "semicolon", "period", "comma", "plus", "minus", "backslash", "slash", "star", "equal",
                    "carat", "leftparen", "rightparen", "id", "integer", "space", "dless", "lesseq", "spaceship", "greatereq",
                    "dgreater", "noteq", "dbang", "string", "coloneq", "dcolon", "dplus", "plusminus",
                    "I made a mistake on the lookup table and am too lazy to fix it" ,
                    "minusplus", "ddash", "slasheq", "eqeq", "fixed",  "comment", "currency", "scinotation" , "file", "library"]

    def getcode(code):
        return codes.lookup_codes[code]