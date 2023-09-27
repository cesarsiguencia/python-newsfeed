var title= document.querySelector('#title')
var trialModal = document.querySelector('#trial-modal')
var closeTrial = document.querySelector('#close-trial')
var firstVisit = true

if(firstVisit){
    console.log('visited')
    setTimeout(function(){
        trialModal.style.height="100vh"
        firstVisit = false
    }, 1000)

}

// title.addEventListener("click", function(){
//     trialModal.style.height="100vh"
// })

closeTrial.addEventListener("click", function(){
    trialModal.style.height="0px"
})