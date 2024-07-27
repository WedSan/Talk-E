class WordSplitter:

    def split_inside_chars(self, text: str, character: str) -> list:
        
        parts = text.split(character)
        
        wordPhrase_list = [part.strip() for index, part in enumerate(parts) if index % 2 != 0 and part.strip()]
        return wordPhrase_list 

    def split_outsite_chars(self, text: str, character: str):

        parts = text.split(character)
        wordPhrase_list = [part.strip() for index, part in enumerate(parts) if index % 2 == 0 and part.strip()]

        return wordPhrase_list


