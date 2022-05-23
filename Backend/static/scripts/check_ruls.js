const privacyCheck = document.querySelector('#privacyCheck')
const form = document.querySelector('#signup-form')

console.log(privacyCheck)
form.addEventListener('submit', e => {
    if (!privacyCheck.checked) {
        e.preventDefault()
        document.querySelector('#privacy').style.display = 'block'
    }
})
