var myName = 'Roman'

function sayAName() {
  var myName = 'Drew'
  console.log('myName inside sayAName is: ' + myName);

}

function sayMyName() {
  var myLastName = 'Korver'
  console.log('myName inside sayMyName is: ' + myName)
  console.log('myLastName inside sayMyName is: ' + myLastName)
}

sayAName();
sayMyName();
console.log('myName outside the function is: ' + myName);
console.log('myLastName outside the function is: ' + myLastName);
