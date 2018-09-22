
var str = "This is an amazing sentence This is .";

function word_counter(message){
    var words = {};
    var w = message.split(" ");

    w.forEach(word => {
        if (words[word]){
            words[word] += 1;
        } else
            words[word] = 1;

    })

    console.log(words)
}

word_counter(str)
