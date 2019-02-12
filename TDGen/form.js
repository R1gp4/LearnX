
function showBarcodes(barcodes) {
var visualOutput = '';
for (i=0; i < barcodes.length; i++) {
  visualOutput +=  barcodes[i] + '<br>' ;
  }
  document.getElementById("output").innerHTML = visualOutput;
}


// grappige tekst
function submitForm() {
  var text= 'Gast. Heb je een PID? Check SVInfo ;)';
  document.getElementById("output").innerHTML = text;
}


// Produceert 'amount' * barcodes
function generateBarcode() {
  var barcodes = [];
  var zeroes = '00000'
  var identifier = document.getElementById("kenmerk").value;
  var testPieceAmount = document.getElementById("amount").value;

  for (i = 0; i < testPieceAmount; i++) {
   var randomNumbers = Math.floor((Math.random() * 99999999) + 10000);
   barcodes.push(identifier + zeroes + randomNumbers);
  }
  showBarcodes(barcodes);
  return barcodes;
}

// Generate a .txt file containing the desired variables
function generateVFormat() {
  var vformat = '';
  var barcodes = generateBarcode();
  var recipientName = document.getElementById("fname").value;
  var recipientPostalCode = document.getElementById("postalcode").value;
  var recipientStreetNr = document.getElementById("streetnr").value;
  var recipientEmail = document.getElementById("emailaddr").value;
  var recipientPhoneNumber = document.getElementById("telnr").value;
  var shipperName = document.getElementById("verladernm").value;
  var shipperNumber = document.getElementById("verladernr").value;
  var SPcode = document.getElementById("SPnr").value;

  for (i=0; i < barcodes.length; i++) {
    vformat +=  'A030 ' + '\r\n' +                  // UAD
                'V010 ' + '\r\n' +
                'V011 ' + '\r\n' +
                'V015 ' + SPcode +  '\r\n'  +
                'V020 ' + barcodes[i] + '\r\n' +
                'V025 ' + '\r\n' +
                'V110 ' + shipperName + '\r\n' +
                'V170 ' + recipientName + '\r\n' +
                'V174 ' + recipientPhoneNumber + '\r\n' + //phoneNumber
                'V176 ' + '\r\n' +
                'V180 ' + recipientStreetNr + '\r\n' +
                'V190 ' + recipientPostalCode + '\r\n' +
                'V191 ' + '\r\n' +                        // city
                'V800 ' + shipperNumber + '\r\n' +
                'V999 ' + '\r\n' +
                'Z999 ' + '\r\n';
  }
  // document.getElementById("message").innerHTML = vformat;
  return vformat;
}

// prepares an e-mail in default Mail application
function sendMail() {
    var messageBody = generateVFormat();
    var subject = document.getElementById("fname").value;
    var txt = '.txt';
    var filename = prompt('Choose your filename:') + txt;
    download(messageBody, filename, 'txt');

    document.location.href = "mailto:it.services@dhl.com?subject="
        + encodeURIComponent(subject)
        + "&body=" + encodeURIComponent('messageBody');

}




//










// function resetForm() {
//   document.getElementById("frm1").reset();
// }
