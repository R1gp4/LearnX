var projectName = 'kittenbook';
var versionNumber = '0.0.1';
var currentDate = new Date(); // Create Date object.

	//currentTime wille look like ' 2014-01-25 at 14:45:12'

var currentTime = 	currentDate.getFullYear() + '-' + 	// set year
			(currentDate.getMonth() +1)+ '-' + 	// set month
			currentDate.getDate() + ' at ' + 	// set day of the month
			currentDate.getHours() + ':' + 		// set hours
			currentDate.getMinutes() + ':' + 	// set minutes
			currentDate.getSeconds() + ;    // set seconds
var userName = prompt('Hello, what\'s your name?');
document.body.innerHTML = '<h1> Hello, ' + userName + '! </h1>' +
				'<p>' + projectName + ' ' + versionNumber +
				' accessed on: ' + currentTime + '</p>';
