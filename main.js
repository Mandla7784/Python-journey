const productLink = document.getElementById("product-link");
const cartLink = document.getElementById("cart-link");

//Pages
const productPage = document.querySelector(".product-page");
const cartPage = document.querySelector(".cart");

//Navigaion

function navigateTo(page) {
  if (page === "product-page") {
    cartPage.classList.add("hidden");
    productPage.classList.remove("hidden");
  } else {
    cartPage.classList.remove("hidden");
    productPage.classList.add("hidden");
  }
}
navigateTo("product-page");

//event listeners
productLink.addEventListener("click", () => {
  navigateTo("product-page");
});

cartLink.addEventListener("click", () => {
  navigateTo("cart");
});
const quantity = 0;
const item = {
  image: document.querySelector("img").src,
  id: Date.now().toString(),
  quantity: quantity,
};

function setItemsToLocal() {
  console.log("Itemem succesfully added !");
  const updatedQuantity = item.quantity++;
  console.log(updatedQuantity);
  localStorage.setItem("cart", JSON.stringify(item));
}

//Adding items to cart
const btnAddItemToCart = document.getElementById("btn-add");

//event...
btnAddItemToCart.onclick = setItemsToLocal;

// Display items from local storage
function displayItems() {
  const cartImage = document.createElement("img");
  const quan = document.createElement("p");
  let list = document.querySelector(".product-list");
  let item = JSON.parse(localStorage.getItem("cart"));
  let { image, quantity } = item;
  cartImage.src = image;

  const removeBtn = document.createElement("button");
  const qyanityBtn = document.createElement("button");
  removeBtn.textContent = "Remove";
  qyanityBtn.textContent = "+";
  quan.textContent = quantity;
  removeBtn.classList.add("remove-btn");

  qyanityBtn.addEventListener("click", () => {
    quantity = quantity + 1;
    quan.textContent = quantity;
  });
  list.append(cartImage, removeBtn, quan, qyanityBtn);
}
displayItems();
