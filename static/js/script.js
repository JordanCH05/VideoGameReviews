document.addEventListener('DOMContentLoaded', starRating);

document.querySelector("#id_score").addEventListener('input', starReviewRating)
    
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
    
    console.log(ratingPercent);
}

/**
* Times out messages to close after a few seconds
    */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);