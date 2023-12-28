class Solution:
    def reverseWords(self, s: str) -> str:
        final_array = []
        array_without_space = []
        s = s.strip()
        word_array = s.split(" ")
        for j in reversed(range(len(word_array))):
            final_array.append(str(word_array[j]).replace(" ", ""))
        for a in final_array:
            if a != '':
                array_without_space.append(a)
        final_str = ' '.join([str(elem) for elem in array_without_space])
        return final_str