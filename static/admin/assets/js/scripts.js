function hideFlash() {
    setTimeout(() => {
        const obj = document.querySelector('#modalMessage')
        obj.className += ' hide'
    } , 3000)
}

hideFlash()