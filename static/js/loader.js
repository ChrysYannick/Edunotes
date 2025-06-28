window.addEventListener("load", () => {
    // Attendre que tout le contenu soit chargé
    setTimeout(() => {
        document.getElementById("loader").style.display = "none";  // Masque le loader
        document.getElementById("page-content").classList.remove("hidden");
        document.getElementById("page-content").style.opacity = 1;  // Affiche le contenu de la page
    }, 900);  // Délai de 3 secondes avant de masquer le loader, tu peux ajuster ce délai
});
