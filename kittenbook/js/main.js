function main() {
  var userName = getUserName();
  var phoneNumber = getPhoneNumber(userName);
  var location = getLocation(phoneNumber);
  images = getImages();


setInterval(function() {
  images = getImages();
  replaceImages(images, location);
  }, 3000);
}

main();


// document.body.innerHTML = '<h1> Hello, ' + userName + '! </h1>' +
// 				'<p>' + kbValues.projectName + ' ' + kbValues.versionNumber +
// 				' accessed on: ' + kbValues.currentTime + '</p>';
