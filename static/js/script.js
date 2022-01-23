document.addEventListener('DOMContentLoaded', starRating);
    
/**
* Styles star rating width based on score
    */
function starRating() {
    
    const scores = document.querySelectorAll(".score")
    for (let score in scores) {
        const rating = scores[score].innerHTML;
        const ratingPercent = (rating / 5) * 100;
        const ratingPercentRounded = `${Math.round
        ((ratingPercent) / 10) * 10}%`;
        document.querySelectorAll(".stars-inner")[score].style.width = ratingPercentRounded;
    }
    
}

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);