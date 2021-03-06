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
