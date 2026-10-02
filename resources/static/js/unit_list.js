
const searchInput = document.getElementById("unitSearch");
const unitCards = document.querySelectorAll(".unit-card");

if (searchInput) {
    searchInput.addEventListener("input", function () {
        const searchText = searchInput.value.toLowerCase().trim();

        unitCards.forEach(function (card) {
            const unitText = card.textContent.toLowerCase();

            card.style.display = unitText.includes(searchText)
                ? "block"
                : "none";
        });
    });
}