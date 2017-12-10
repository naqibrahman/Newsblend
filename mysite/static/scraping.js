function loadArticleText(){
    articleID = this.classList[1];
    if (! this.classList.contains("scraped")){
        this.classList.add("scraped")
        req = new XMLHttpRequest();
        url = "article/"+articleID;
        req.open('GET', url)
        req.addEventListener('load', function(evt) {
            if(req.status >= 200 && req.status < 300) {
                console.log(req.responseText)
                const textDiv = document.querySelector("#articleText_"+articleID)
                textDiv.innerHTML =  req.responseText
            }
        })
        req.send();    
        

    }


}

function main(){
    const btns = document.querySelectorAll(".loadArticle");
    for (let i = 0; i < btns.length; ++i) {
        btns[i].addEventListener("click",loadArticleText.bind(btns[i]));
    }
    
}

document.addEventListener('DOMContentLoaded', main);