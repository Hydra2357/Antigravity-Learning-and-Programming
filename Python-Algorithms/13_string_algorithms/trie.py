"""
Trie (Prefix Tree) Implementation
An ordered tree data structure used to store a dynamic set of strings, where keys are usually strings.
Time Complexities:
    - Insert: O(L) where L is length of word
    - Search: O(L)
    - StartsWith: O(L)
    - Delete: O(L)
Space Complexity: O(ALPHABET_SIZE * L * N) where N is number of words, L is average length.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Returns True if the word is in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """Deletes a word from the trie. Returns True if deleted."""
        def _delete_helper(node, word, depth):
            if depth == len(word):
                # Word end reached. Unmark end of word
                if not node.is_end_of_word:
                    return False  # Word wasn't present
                node.is_end_of_word = False
                # If node has no children, it can be deleted
                return len(node.children) == 0
                
            char = word[depth]
            if char not in node.children:
                return False  # Word not present
                
            should_delete_child = _delete_helper(node.children[char], word, depth + 1)
            
            if should_delete_child:
                del node.children[char]
                # Return True if current node can also be deleted
                return not node.is_end_of_word and len(node.children) == 0
                
            return False
            
        return _delete_helper(self.root, word, 0)

if __name__ == "__main__":
    print("=== Trie Prefix Tree Demo ===")
    trie = Trie()
    
    words = ["apple", "app", "apricot", "banana", "bat"]
    print(f"Inserting words: {words}")
    for w in words:
        trie.insert(w)
        
    print("\nSearch tests:")
    print(f"  Search 'apple':   {trie.search('apple')} (Expected: True)")
    print(f"  Search 'app':     {trie.search('app')} (Expected: True)")
    print(f"  Search 'appl':    {trie.search('appl')} (Expected: False)")
    print(f"  Search 'apricot': {trie.search('apricot')} (Expected: True)")
    
    print("\nPrefix 'startsWith' tests:")
    print(f"  Prefix 'ap':  {trie.starts_with('ap')} (Expected: True)")
    print(f"  Prefix 'ban': {trie.starts_with('ban')} (Expected: True)")
    print(f"  Prefix 'cat': {trie.starts_with('cat')} (Expected: False)")
    
    print("\nDeleting 'app'...")
    trie.delete("app")
    print(f"  Search 'app':   {trie.search('app')} (Expected: False)")
    print(f"  Search 'apple': {trie.search('apple')} (Expected: True)")
