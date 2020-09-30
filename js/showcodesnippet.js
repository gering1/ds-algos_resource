function showCode(code,button) {
    sol_button = document.querySelector(button)
    txt = document.querySelector(code);
    txt.style.display == "block" ? txt.style.display = "none" : txt.style.display = "block"
    sol_button.innerText == "Show Solution" ? sol_button.innerText = "Hide Solution" : sol_button.innerText = "Show Solution"
}