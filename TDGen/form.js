
function showBarcodes(barcodes) {
var visualOutput = '';
for (i=0; i < barcodes.length; i++) {
  visualOutput +=  barcodes[1] + '<br>' ;
  }
  document.getElementById("output").innerHTML = visualOutput;
}


// grappige tekst
function submitForm() {
  var text= 'Gast. Heb je een PID? Check SVInfo ;)';
  // document.getElementById("frm1").submit();
  document.getElementById("output").innerHTML = text;
}


// Produceert 'amount' * barcodes
function generateBarcode() {
  var barcodes = [];
  var zeroes = '00000'
  var identifier = document.getElementById("kenmerk").value;
  var testPieceAmount = document.getElementById("amount").value;

  for (i = 0; i < testPieceAmount; i++) {
   var randomNumbers = Math.floor((Math.random() * 999999999) + 10000);
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
  var shipperName = document.getElementById("shname").value;

  for (i=0; i < barcodes.length; i++) {
    vformat +=  'A030 UAD' + '\r\n' +
                'V010 ' + '\r\n' +
                'V011 ' + '\r\n' +
                'V015 ' + 'NL-306261' +  '\r\n'  +
                'V020 ' + barcodes[i] + '\r\n' +
                'V025 ' + '\r\n' +
                'V110 ' + shipperName + '\r\n' +
                'V170 ' + recipientName + '\r\n' +
                'V174 ' + 'recipientPhoneNumber' + '\r\n' + //phoneNumber
                'V176 ' + '\r\n' +
                'V180 ' + recipientStreetNr + '\r\n' +
                'V190 ' + recipientPostalCode + '\r\n' +
                'V191 ' + 'Recipient city' + '\r\n' +
                'V800 ' + '79561103' + '\r\n' +
                'V999  Z' + '\r\n' +
                'Z999  Z' + '\r\n';
  }
  // document.getElementById("message").innerHTML = vformat;
  return vformat;
}


function sendMail() {
    var messageBody = generateVFormat();
    var subject = document.getElementById("fname").value;
    document.location.href = "mailto:it.services@dhl.com?subject="
        + encodeURIComponent(subject)
        + "&body=" + encodeURIComponent(messageBody);

}

//
// // download text file (not yet well configured)
// function barcodeView(text, name, type) {
//     var a = document.getElementById("a");
//     var file = new Blob([text], {type: type});
//     a.href = URL.createObjectURL(file);
//     a.download = name;
//   }









// function resetForm() {
//   document.getElementById("frm1").reset();
// }
