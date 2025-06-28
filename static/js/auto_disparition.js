// Attendre que la page soit chargée
document.addEventListener("DOMContentLoaded", function () {
     // Cibler tous les messages
     const alerts = document.querySelectorAll('.alert');
     alerts.forEach(alert => {
         setTimeout(() => {
             alert.style.opacity = '0';
             alert.style.transform = 'translateY(-10px)';
             alert.style.transition = 'all 0.5s ease';

             // Supprimer l'élément du DOM après l'animation
             setTimeout(() => {
                 alert.remove();
             }, 500);
         }, 2000); // délai en ms avant disparition (4 secondes ici)
     });
 });