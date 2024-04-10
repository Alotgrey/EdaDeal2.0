document.getElementById("open-category-popup-btn").addEventListener("click",function(){
    document.getElementById("category-popup-id").classList.add("open")
}) 

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("category-popup-id").classList.remove("open")
    }
});

document.querySelector("#category-popup-id .box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("category-popup-id").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});