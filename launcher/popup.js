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
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id, allFrames: true},
        files: ['content_scripts/script.js'],
      });
        
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
             Array.from(data).map(i => {
                let parsedA = parser.parseFromString(i.innerHTML, 'text/html')
                let h3Main = parsedA.getElementsByTagName("h3")
                console.log(i.classList, i.id, i.className)
                if(h3Main.length > 0) {
                    window.fetch(`${API_BASE_URL}/verify`, {
                        method: "POST",
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ url: i.href })
                    })
                    .then(async(_res) => {
                        const res = await _res.json();
                        console.log(res.result, h3Url)
                        // if (res.result === 0) {
                        //     injectGreenTick(i);
                        // } else if (res.result === 1) {
                        //     injectRedCross(i);
                        // }
                    })
                    .catch(err => console.warn(err.toString()))
                }
            })
        })
        .catch(err => console.warn(err.toString()));

        
    });
}
