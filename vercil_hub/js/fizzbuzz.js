function fizzbuzz(){
    for (var i = 1; i <= 100; i++) {
        var output = ""
        if (i % 3 == 0) {output += "Fizz";}
        if (i % 5 == 0) {output += "Buzz";} 
        // if (i % 7 == 0) {output += "Huzz";}
        if (output == "") {output = i;}
        console.log(output)
    }
}
fizzbuzz()