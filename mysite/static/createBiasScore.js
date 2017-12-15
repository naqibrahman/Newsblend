function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  }

function createBiasScore(articleId){
    var csrftoken = getCookie('csrftoken')    
    var score = document.getElementById("biasScore-"+articleId).value;
    var req= new XMLHttpRequest();
    req.open('POST', 'createbiasscore/', true);
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    req.setRequestHeader("X-CSRFToken", csrftoken);
    req.addEventListener('load', function(evt){
        console.log("ajax post successful");
    })
    req.send('score=' + score + '&articleid=' + articleId);
    return true;
}
