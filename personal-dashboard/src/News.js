import React, { useEffect, useState } from "react"; 

let apiUrl = "https://api.nytimes.com/svc/topstories/v2";
let apiKey = "bwS9ACyhdCzN0pQIGsZO9s8EfQ1xlMpR";
let type = "world.json";   

function News () {
    const [news, setNews] = useState(null); 
    useEffect(() => {
        let api = `${apiUrl}/${type}?api-key=${apiKey}`;
        fetch(api).then(response => response.json()).then(data => {
            setNews(data); 
        })  
    }, []);
    return (
        news && news.results.splice(0, 5).map((article, index) => {
            return (
                <article key = {article.url}>
                    <a href = {article.url}>{article.title}</a> 
                </article>
            ) 
        })
    );
}

export default News; 