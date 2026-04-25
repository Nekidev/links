let apiHost;

if (window.location.hostname == "localhost" || window.location.hostname == "127.0.0.1") {
    apiHost = "http://127.0.0.1:8000";
} else {
    apiHost = "https://nye.lat";
}

const form = document.querySelector("#form");
const input = document.querySelector("#url");
const results = document.querySelector("#results");

async function onSubmit(e) {
    e.preventDefault();

    let long = input.value;

    let response = await fetch(`${apiHost}/links`, {
        method: "POST",
        body: JSON.stringify({ location: long }),
        headers: {
            "Content-Type": "application/json",
        },
    });
    let data = await response.json();

    if (!response.ok) {
        alert("We couldn't generate your URL!");
        return;
    }

    showResult(long, data.shortened);
}

function showResult(long, short) {
    let result = document.createElement("div");
    result.classList.add("result");

    result.innerText = `${short} <- ${long}`;
    results.appendChild(result);
}

form.addEventListener("submit", onSubmit);
