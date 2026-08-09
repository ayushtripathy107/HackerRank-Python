import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        // 1. Put banned words in a set for O(1) lookups
        Set<String> bannedSet = new HashSet<>();
        for (String word : banned) {
            bannedSet.add(word);
        }
        
        // 2. Normalize string: lower case and replace punctuation with spaces
        // This regex matches any character that is NOT a lowercase letter, uppercase letter, or digit
        String normalizedStr = paragraph.replaceAll("[^a-zA-Z0-9 ]", " ").toLowerCase();
        
        // 3. Split by one or more spaces
        String[] words = normalizedStr.split("\\s+");
        
        // 4. Count frequencies of non-banned words
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            if (!word.isEmpty() && !bannedSet.contains(word)) {
                wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
            }
        }
        
        // 5. Find the word with the highest frequency
        String mostCommon = "";
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            if (entry.getValue() > maxCount) {
                mostCommon = entry.getKey();
                maxCount = entry.getValue();
            }
        }
        
        return mostCommon;
    }
}
