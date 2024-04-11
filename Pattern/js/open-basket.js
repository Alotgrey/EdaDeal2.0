document.getElementById("open-basket-popup-btn").addEventListener("click",function(){
    document.getElementById("basket-popup-id").classList.toggle("open")
}) 

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("basket-popup-id").classList.remove("open")
    }
});
