var letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];

var new_arr = [];


for(var i=0;i<letters.length;i++) {
    var x = letters[i];
    var y = Math.floor((Math.random() * 10) + 0);
    new_arr.push(x + "=" + y);
    
}

console.log(new_arr)
