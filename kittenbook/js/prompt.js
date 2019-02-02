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
		phoneNumber = prompt('Hey Poopoohead ' + userName + 'how about a real phone number?');
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

// function getLocation() {
// 	var location =
// }
//Get the user's location based on phone versionNumber
// if getPhoneNumber === /w/
//
// document.body.innerHTML = '<h1> Hello, ' + userName + '! </h1>' +
// 				'<p>' + kbValues.projectName + ' ' + kbValues.versionNumber +
// 				' accessed on: ' + kbValues.currentTime + '</p>';
