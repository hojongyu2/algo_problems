var isPalindrome = function(s) {
    let removedLetters = s.replace(/[^a-z0-9]/gi, "").toLowerCase()
    let begin = 0;
    let end = removedLetters.length -1;
    while(begin < end){
        let beginChar = removedLetters[begin]
        let endChar = removedLetters[end]
        if(beginChar !== endChar){
            return false
        }
        begin++
        end--
    }
    return true
};