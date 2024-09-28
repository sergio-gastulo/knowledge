var first_name = "sergiog"
let last_name = "gastulo"
const full_name = "sergio_gastulo"

//which can you change?

first_name = "hi"
last_name = "hi"

// definitely not this one - at least globally
//full_name = "hi" 

console.log(first_name + last_name)

//more garbage 
function run() {
    var foo = "Foo";
    let bar = "Bar";
  
    console.log(foo, bar); // Foo Bar
  
    {
      var moo = "Mooo"
      let baz = "Bazz";
      console.log(moo, baz); // Mooo Bazz
    }
  
    console.log(moo); // Mooo
    console.log(baz); // ReferenceError
  }
  
  run();

  //further info
  //https://stackoverflow.com/questions/762011/what-is-the-difference-between-let-and-var

  