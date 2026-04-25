let apiHost;

if (
    window.location.hostname == "localhost" ||
    window.location.hostname == "127.0.0.1"
) {
    apiHost = "http://127.0.0.1:8000";
} else {
    apiHost = "https://nye.lat";
}

const form = document.querySelector("#form");
const input = document.querySelector("#url");
const inputSubmit = document.querySelector("#submit");
const results = document.querySelector("#results");
const resultsEmpty = document.querySelector("#results-empty");
const resultsClear = document.querySelector("#results-clear");

function alert(message) {
    let alertElement = document.createElement("div");
    alertElement.classList.add("alert");

    alertElement.innerText = message;

    document.body.appendChild(alertElement);

    setTimeout(() => {
        alertElement.remove();
    }, 5000);
}

async function onSubmit(e) {
    e.preventDefault();

    try {
        inputSubmit.innerText = "Shortening URL...";

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
            alert(data.message);
            return;
        }

        showResult(long, data.shortened);
    } finally {
        inputSubmit.innerText = "Shorten URL";
    }
}

function showResult(long, short) {
    let result = document.createElement("button");
    result.classList.add("result");

    let resultLong = document.createElement("div");
    resultLong.classList.add("result-long");
    resultLong.innerText = long;

    let resultShort = document.createElement("div");
    resultShort.classList.add("result-short");
    resultShort.innerText = short;

    result.appendChild(resultLong);
    result.appendChild(resultShort);

    result.addEventListener("click", (e) => {
        navigator.clipboard.writeText(short);
        alert("Copied to clipboard!");
    });

    results.appendChild(result);

    resultsEmpty.classList.add("hidden");
    resultsClear.removeAttribute("disabled");
}

form.addEventListener("submit", onSubmit);

function clearResults() {
    resultsEmpty.classList.remove("hidden");
    resultsClear.setAttribute("disabled", "true");
    results.replaceChildren();
}

resultsClear.addEventListener("click", clearResults);
