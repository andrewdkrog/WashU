var movieScore = [4.4, 3.3, 5.9, 8.8, 1.2, 5.2, 7.4, 7.5, 7.2, 9.7, 4.2, 6.9];

function statistics(x){
    var tally = 0;

    for (i=0; i<x.length; i++){
        tally =+ x[i];
        console.log(tally);
    }
}
statistics(movieScore);
