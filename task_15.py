class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt = False):
        self.decrypt = decrypt
        if isinstance(text, str):
            self.text = text
        else:
            raise ValueError("string only!")
        if not isinstance(key, str) or not (key.isalpha() and key.isascii()):
            raise ValueError("latin alphabet only!")
        if len(set(key.lower())) == len(key.lower()):
               self.key = key.lower()
        else:
            raise ValueError("unique chars only!")
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
            new_blocks[-1] = new_blocks[-1].rstrip()
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

