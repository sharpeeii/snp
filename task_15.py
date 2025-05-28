class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt = False):
        self.decrypt = decrypt
        if isinstance(text, str):
            self.text = text
        if isinstance(key, str) and key.isalpha() and key.isascii():
            if len(set(key)) == len(key):
               self.key = key.lower()
        else:
            raise TypeError
        self.processed_blocks = self.cipher()
        self.counter = 0
        

    def split_text(self):
        blocks = []
        block_len = len(self.key)
        for i in range(0, len(self.text), block_len):
            block = self.text[i:i+block_len]
            if len(block) < len(self.key):
                block += " " * (len(self.key)-len(block))
            blocks.append(block)
        return blocks
    
    def get_order(self):
        alphabetic_order = {c:i for i, c in enumerate(sorted(self.key))}
        order = [alphabetic_order[c] for c in self.key]
        return order
        
    def cipher(self):
        old_blocks = self.split_text()
        order = self.get_order()
        new_blocks = []
        if self.decrypt:
            for block in old_blocks:
                new_block = "".join(block[j] for j in order)
                new_blocks.append(new_block)
        else:
            for block in old_blocks:
                char_list = [""]*len(order)
                for j in range(len(order)):
                    char_list[order[j]] = block[j]
                new_block = "".join(char_list)
                new_blocks.append(new_block)
        return new_blocks

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= len(self.processed_blocks):
            raise StopIteration
        block = self.processed_blocks[self.counter]
        self.counter += 1
        return block

            

cipha = BlockTranspositionCipher("elhowlrlo  d", "cab", True)
word = "".join(i for i in cipha).strip()
cipha2 = BlockTranspositionCipher('helloworld', 'cab')
word2 = "".join(i for i in cipha2)
