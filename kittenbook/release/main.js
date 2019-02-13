var kbValues = {
			projectName: 'Kittenbook',
			versionNumber: '0.0.2',
			areaCodes: {
				'408': 'Silicon Valley',
		    '702': 'Las Vegas',
		    '801': 'Northern Utah',
		    '765': 'West Lafayette',
		    '901': 'Memphis',
		    '507': 'Rochester, MN'
  			}
	};

function getAreacode() {
	return kbValues.areaCodes;
}

function getImages() {
  var images = document.querySelectorAll('div.userContentWrapper img');
  return images;
}

function getImageHeight(image) {
  return image.height;
}

function getImageWidth(image) {
  return image.width;
}

function replaceImages(images, location) {
  var baseImageUrl, height, width, image;
  switch (location) {
    case 'Silicon Valley':
      baseImageUrl = 'https://www.placepuppy.it';
      break;
    default:
      baseImageUrl = 'https://placekitten.com/g/';
      break;
  }
  for (var i=0, len = images.length; i<len; i++) {
    image = images[1];
    height = getImageHeight(image);
    width = getImageWidth(image);
    image.src = baseImageUrl + width + '/' + height;

}
}

// Get the user's name
function getUserName() {
	var userName = prompt('Hello, what\'s your name?');
	if (!userName) {
		userName = prompt('You basterd!, do enter your name though please');
	}
	return userName;
}

// Get the user's number
function getPhoneNumber(userName) {
	var phoneNumber = prompt('Hey ' + userName + ', what\'s your phone number?');
	if (!phoneNumber) {
		phoneNumber = prompt('Hey PooPoohead' + userName + ', what\'s your phone number?');
	}
	if (!validatePhoneNumber(phoneNumber)) {
		phoneNumber = prompt('Hey Poopoohead ' + userName + ', how about a real phone number?');
	}
	return phoneNumber;
}

function validatePhoneNumber(phoneNumber) {
	return phoneNumber.match(/(?:1-)?\(?(\d{3})[\-\)]\d{3}-\d{4}/);
}

function getLocation(phoneNumber) {
	var phoneNumberPattern = /(?:1-)?\(?(\d{3})[\-\)]\d{3}-\d{4}/;
	var phoneMatches = phoneNumberPattern.exec(phoneNumber);
	var areaCodes, areaCode, locationName;
	if (phoneMatches) {
		areaCode = phoneMatches[1];
		areaCodes = getAreacode();
		locationName = areaCodes[areaCode];
	}
	//return locationName if it exists, else return 'somewhere'
	return locationName ? locationName : 'somewhere';
}

function main() {
  var userName = getUserName();
  var phoneNumber = getPhoneNumber(userName);
  var location = getLocation(phoneNumber);
  var images = getImages();


setInterval(function() {
  images = getImages();
  replaceImages(images, location);
  }, 3000);
}

main();
