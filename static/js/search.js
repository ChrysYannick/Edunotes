function filterByType() {
     let type = document.getElementById("typeFilter").value.toLowerCase();
     let rows = document.querySelectorAll("#sortableTable tbody tr");
 
     rows.forEach(row => {
         let typeCell = row.querySelector("td[data-type]");
         if (!type || (typeCell && typeCell.textContent.toLowerCase().includes(type))) {
             row.style.display = "";
         } else {
             row.style.display = "none";
         }
     });
 }
