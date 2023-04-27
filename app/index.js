function requestApi(){
  fetch('/api')
  .then(function(response) {
    return response.json()
  }).then(function(data){
    dataManipulation(data)
  }).catch(function (err){
    console.warn(err)
  })
}

function dataManipulation(data){
  let jsonParseData = JSON.parse(data)
  let {routes} = jsonParseData
  let keys = Object.keys(routes)
  let root = document.getElementById("root")
  routesManipulation(keys,routes,root)
}

function routesManipulation(keys,routes,root){
  for(k in keys){
    if(window.location.pathname === keys[k]){
      jsonParse = routes[keys[k]]
      root.innerHTML = jsonParse.html
      addCSS(jsonParse.css)
  
    }
  }
  addTitle(routes.title)
}

function addCSS(css){
  document.head.appendChild(
    document.createElement("style")
  ).innerHTML = css
}

function addTitle(title){
  document.head.appendChild(
    document.createElement("title")
  ).innerHTML = title
}

requestApi()