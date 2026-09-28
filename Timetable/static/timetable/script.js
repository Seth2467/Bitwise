const searchInput = document.getElementById("timetableSearch");
const timetableRows = document.querySelectorAll(".timetable-row");
const daySections = document.querySelectorAll(".day-selection");
const dayFilter = document.getElementById("dayFilter");

function filterTimetable() {
    const searchText = searchInput.value.toLowerCase();
    const selectedDay = dayFilter.value;

    timetableRows.forEach(function (row) {
        const searchData = row.dataset.search.toLowerCase();
        const rowDay = row.dataset.day;
        const rowMatchesSearch = searchData.includes(searchText);
        const rowMatchesDay = selectedDay === "All" || rowDay === selectedDay;

        if (rowMatchesSearch && rowMatchesDay) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });

    daySections.forEach(function (section){
        const sectionDay = section.dataset.day;

        if (selectedDay === "All" || sectionDay === selectedDay) {
            section.style.display = "";
        } else {
            section.style.display = "none";
        }
    });
}

searchInput.addEventListener(
    "input",
    filterTimetable
);

dayFilter.addEventListener(
    "change",
    filterTimetable
);