const titleEl = document.querySelector('.product-form__title');
const titleCounter = titleEl.nextElementSibling;
const maxTitleLength = titleEl.maxLength;
const updateTitleCounter = (e) => {
  const len = e ? e.target.value.length : 0;
  titleCounter.textContent = `${len} / ${maxTitleLength}`;
}
updateTitleCounter();
titleEl.addEventListener('keyup', updateTitleCounter);
titleEl.addEventListener('keydown', updateTitleCounter);

const descriptionEl = document.querySelector('.product-form__description');
const descriptionCounter = descriptionEl.nextElementSibling;
const maxDescriptionLength = descriptionEl.maxLength;
const updateDescriptionCounter = (e) => {
  const len = e ? e.target.value.length : 0;
  descriptionCounter.textContent = `${len} / ${maxDescriptionLength}`;
}
updateDescriptionCounter();
descriptionEl.addEventListener('keyup', updateDescriptionCounter);
descriptionEl.addEventListener('keydown', updateDescriptionCounter);