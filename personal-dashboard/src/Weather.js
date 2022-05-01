import React, { useEffect, useState } from "react"; 

let apiUrl = "https://api.openweathermap.org/data/2.5/weather";
let apiKey = "b960e657d88a137a88622a486f8bd92c"; 
let city = "Mountain View, USA" 

function Weather () {
    const [weather, setWeather] = useState(null); 
    useEffect (() => {
        let api = `${apiUrl}?q=${city}&appid=${apiKey}&units=imperial`;
        fetch(api).then(response => response.json()).then(data => {
            setWeather(data);
        })
    }, []);
    return (
        <h2>It is currently {weather && weather.main.temp}° in {city}.</h2> 
    );
}

export default Weather; 