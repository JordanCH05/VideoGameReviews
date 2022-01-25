document.addEventListener('DOMContentLoaded', starRating);

if (document.querySelector("#id_score")) {
    document.querySelector("#id_score").addEventListener('input', starReviewRating);
}
    
/**
* Styles star rating width based on score
    */
function starRating() {
    
    const scores = document.querySelectorAll(".score");
    const star_ratings = document.querySelectorAll(".stars-inner");
    for (let score in scores) {
        const rating = scores[score].innerHTML;
        if (rating) {
            const ratingPercent = (rating / 5) * 100;
            const ratingPercentRounded = `${Math.round
            ((ratingPercent) / 10) * 10}%`;
            star_ratings[score].style.width = ratingPercentRounded;
        }
    }
    
}

/**
* Styles star rating width based on score input
    */
function starReviewRating() {

    const score_input = document.querySelector("#id_score").value;
    const star_ratings = document.querySelectorAll(".stars-inner");
    const star_rating = star_ratings[star_ratings.length - 1];
    if (score_input >= 0 && score_input <= 5) {
        const ratingPercent = (score_input / 5) * 100;
        const ratingPercentRounded = `${Math.round
            ((ratingPercent) / 10) * 10}%`;
        star_rating.style.width = ratingPercentRounded;
    }
}

/**
* Times out messages to close after a few seconds
    */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);