// // download text file (not yet well configured)
// function creatTextFile(text, name, type) {
//     var a = document.getElementById("a");
//     var file = new Blob([text], {type: type});
//     a.href = URL.createObjectURL(file);
//     a.download = name;
//   }


  // Function to download data to a file
  function download(data, filename, type) {
      var file = new Blob([data], {type: type});
      if (window.navigator.msSaveOrOpenBlob) // IE10+
          window.navigator.msSaveOrOpenBlob(file, filename);
      else { // Others
          var a = document.createElement("a"),
                  url = URL.createObjectURL(file);
          a.href = url;
          a.download = filename;
          document.body.appendChild(a);
          a.click();
          setTimeout(function() {
              document.body.removeChild(a);
              window.URL.revokeObjectURL(url);
          }, 0);
      }
  }
