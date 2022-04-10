// let API_BASE_URL = "https://gauthamkrishna.pythonanywhere.com"
let API_BASE_URL="http://127.0.0.1:5000"
console.warn("YESHSHHHHH")
console.warn(document.title)
const aTags = document.getElementsByTagName("a")
let parser = new DOMParser()


const injectGreenTick = (parentNode) => {
    parentNode.style.display = "flex"
    parentNode.style.marginTop = "30px"
    parentNode.innerHTML = parentNode.innerHTML + `<div style="height: 20px; border-radius: 1000px; width: 20px; background-color: rgb(0, 175, 0); color: white; display: flex; align-items: center; justify-content: center;">&#10004;</div>`
}

const injectRedCross = (parentNode) => {
    parentNode.style.display = "flex"
    parentNode.style.marginTop = "30px"
    parentNode.innerHTML = parentNode.innerHTML + `<div style="height: 20px; border-radius: 1000px; width: 20px; background-color: tomato; color: white; display: flex; align-items: center; justify-content: center;">&#10539;</div>`
}

Array.from(aTags).map(i => {
    let parsedA = parser.parseFromString(i.innerHTML, 'text/html')
    let h3Main = parsedA.getElementsByTagName("h3")
    if(h3Main.length > 0) {
        window.fetch(`${API_BASE_URL}/verify`, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: i.href })
        })
        .then(async(_res) => {
            const res = await _res.json();
            console.log(res.result, i.href)
            if (res.result === 1) {
                injectGreenTick(i);
            } else if (res.result === 0) {
                injectRedCross(i);
            }
        })
        .catch(err => console.warn(err.toString()))
    }
})