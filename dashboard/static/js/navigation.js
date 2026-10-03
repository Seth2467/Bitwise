const menuButton = document.getElementById("menuButton");
const navigationMenu = document.getElementById("navigationMenu");

if (menuButton && navigationMenu) {
    menuButton.addEventListener("click", function () {
        navigationMenu.classList.toggle("open");
    });

    document.addEventListener("click", function (event) {
        if (
            !navigationMenu.contains(event.target) &&
            !menuButton.contains(event.target)
        ) {
            navigationMenu.classList.remove("open");
        }
    });
}