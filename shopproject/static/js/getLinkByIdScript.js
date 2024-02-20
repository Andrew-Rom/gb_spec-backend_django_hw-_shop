const inputOrderEl = document.querySelector(".client_orders__input");
const btnOrderEl = document.querySelector(".client_orders__button");

function getLinkToOrderList() {
  try {
    if (inputOrderEl.value.length === 0
        || Number.isNaN(Number(inputOrderEl.value))
        || Number(inputOrderEl.value) <= 0) {
      throw new Error("Некорректный идентификатор");
    }
    btnOrderEl.href = `/client/${parseInt(inputOrderEl.value)}/orders`
  } catch (error) {
    alert(error.message);
  }
}

inputOrderEl.addEventListener("change", getLinkToOrderList)


const inputProdEl = document.querySelector(".client_products__input");
const btnProdEl = document.querySelector(".client_products__button");

function getLinkToProductList() {
  try {
    if (inputProdEl.value.length === 0
        || Number.isNaN(Number(inputProdEl.value))
        || Number(inputProdEl.value) <= 0) {
      throw new Error("Некорректный идентификатор");
    }
    btnProdEl.href = `/client/${parseInt(inputProdEl.value)}/products`
  } catch (error) {
    alert(error.message);
  }
}

inputProdEl.addEventListener("change", getLinkToProductList)