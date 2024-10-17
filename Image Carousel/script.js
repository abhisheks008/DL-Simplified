const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');
const carouselImages = document.querySelector('.carousel-images');

let currentIndex = 0;

function showImage(index) {
  const totalImages = carouselImages.children.length;
  if (index < 0) {
    currentIndex = totalImages - 1;
  } else if (index >= totalImages) {
    currentIndex = 0;
  } else {
    currentIndex = index;
  }
  const offset = -currentIndex * 100;
  carouselImages.style.transform = `translateX(${offset}%)`;
}

prevButton.addEventListener('click', () => showImage(currentIndex - 1));
nextButton.addEventListener('click', () => showImage(currentIndex + 1));

// Auto-slide every 3 seconds
setInterval(() => showImage(currentIndex + 1), 3000);
