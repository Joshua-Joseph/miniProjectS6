// let API_BASE_URL = "https://gauthamkrishna.pythonanywhere.com"
let API_BASE_URL="http://127.0.0.1:5000"

document.addEventListener('DOMContentLoaded', function() {
    var scannerBtn = document.getElementById('scanner');
    scannerBtn.addEventListener('click', () => {
        verifyUrls();
    });
});

const verifyUrls = () => {
    chrome.tabs.query({currentWindow: true, active: true}, (tabs) => {
        
        let parser = new DOMParser()
        window.fetch(tabs[0].url, {
            method: "GET",  
            headers: { 'Content-Type': 'text/plain' }
        })
        .then(async(res) => {
            let text = await res.text()
            let doc = parser.parseFromString(text,'text/html')
            return doc.getElementsByTagName("a")
            // return doc.body.innerText.replace(/\s/g,'')
        })
        .then(data => {
            let final = []
             Array.from(data).map(i => {
                let parsedA = parser.parseFromString(i.innerHTML, 'text/html')
                let h3Main = parsedA.getElementsByTagName("h3")
                if(h3Main.length > 0) {
                    final.push(i.href)
                }
            })
            console.log(final)
            window.fetch(`${API_BASE_URL}/verify`, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ urls: final })
        })
        .then(async(res) => {
            const pythonResponse = await res.json();
            if (pythonResponse.success) {
                window.location.href = "results.html"
            } else {
                window.location.href = "error.html"
            }
        })
        .catch(err => console.warn(err.toString()))
        })
        .catch(err => console.warn(err.toString()));

        
    });
}
