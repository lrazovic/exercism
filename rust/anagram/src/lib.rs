use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let mut results: HashSet<&'a str> = HashSet::new();
    let mut word_chars: Vec<char> = word.to_lowercase().chars().collect();
    word_chars.sort();
    for anagram in possible_anagrams {
        if anagram.to_lowercase() == word.to_lowercase() {
            continue;
        }
        let mut anagram_vec: Vec<char> = anagram.to_lowercase().chars().collect();
        anagram_vec.sort();
        if word_chars == anagram_vec {
            results.insert(anagram);
        }
    }
    results
}
