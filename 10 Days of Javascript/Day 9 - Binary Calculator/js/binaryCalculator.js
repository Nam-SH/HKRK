function zero() {
  document.getElementById("res").innerText += '0'
}

function one() {
  document.getElementById("res").innerText += '1'
}

function reset() {
  document.getElementById("res").innerText = ''
}

function equal() {
  if (document.getElementById("res").innerText) {
    document.getElementById("res").innerText = eval(document.getElementById("res").innerText)
  }
}

function add() {
  document.getElementById("res").innerText += '+'
}

function sub() {
  document.getElementById("res").innerText += '-'
}

function mul() {
  document.getElementById("res").innerText += '*'
}

function division() {
  document.getElementById("res").innerText += '/'
}